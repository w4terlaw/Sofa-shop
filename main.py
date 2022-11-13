from flask import Flask, render_template, request, redirect, url_for, session, jsonify, json
from flask_mysqldb import MySQL, MySQLdb
import re
import datetime
from passlib.hash import sha256_crypt

from db_CRUD import execute_read_query, execute_query

app = Flask(__name__)

app.secret_key = 'super secret key'
app.permanent_session_lifetime = datetime.timedelta(seconds=600)
mysql = MySQL(app)


# Connect DB
def create_connection(host, user, password, db):
    connection = False
    try:
        app.config['MYSQL_HOST'] = host
        app.config['MYSQL_USER'] = user
        app.config['MYSQL_PASSWORD'] = password
        app.config['MYSQL_DB'] = db
        app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
        print("Connection to MySQL DB successful")
        connection = True
        return connection

    except MySQLdb.OperationalError as e:
        print(f'MySQL server has gone away: {e}, trying to reconnect')
        raise e


connect_db = create_connection('localhost', 'root', 'root', 'sofa_shop')


# Show lesson on page
@app.route('/reg', methods=['GET', 'POST'])
def reg():
    msg = ''
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = sha256_crypt.encrypt(request.form['password'])

        check_sql = f'''select * from user where email = "{email}"'''
        account = execute_read_query(connect_db, check_sql)

        if account:
            msg = 'Этот никнейм уже занят.'
        # elif len(request.form['nickname']) < 4:
        #     msg = 'Никнейм должен содержать не менее 4 символов.'
        # elif not re.match(r'[A-Za-z]', nickname):
        #     msg = 'Никнейм может содержать только латинские буквы.'
        elif not re.match(r'[А-Яа-я]', first_name or last_name):
            msg = 'Имя и фамилия могут содержать только кириллицу.'
        elif first_name[0].islower() or last_name[0].islower():
            msg = 'Имя и фамилия должны начинаться с заглавных букв.'
        elif len(request.form['password']) < 8:
            msg = 'Пароль должен содержать не менее 8 символов.'
        else:
            write_sql = f'''INSERT INTO `user` (`email`, `password`, `first_name`, `last_name`) 
            VALUES ('{email}', '{password}', '{first_name}', '{last_name}')'''
            execute_query(connect_db, write_sql)
            return redirect(url_for('login'))
    return render_template('registration.html', msg=msg)


# Registration
@app.route('/login', methods=['GET', 'POST'])
def login():
    # print(request.url_root + 'login')
    if (request.referrer != request.url_root + 'login') and (request.referrer != request.url_root + 'reg'):
        session['request'] = request.referrer

    print(session.get('request'))
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']

        check_sql = f'''select * from user where email = "{email}"'''
        login_user = execute_read_query(connect_db, check_sql)
        if login_user == tuple():
            msg = 'Неверный никнейм или пароль.'
        else:
            login_user = login_user[0]
            if sha256_crypt.verify(password, login_user['password']):
                # if login_user['teacher']:
                #     session['logged_in'] = True
                #     session['id'] = login_user['id']
                #     session['first_name'] = login_user['first_name']
                #     session['nickname'] = login_user['email']
                #     return redirect(url_for('check_lessons'))
                # else:
                session['logged_in'] = True
                session['first_name'] = login_user['first_name']
                session['last_name'] = login_user['last_name']
                session['nickname'] = login_user['email']
                session['user_id'] = login_user['id']
                if session.get('request') != None:
                    return redirect(session.get('request'))
                return redirect(url_for('home'))
            else:
                msg = 'Неверный никнейм или пароль.'
    return render_template('login.html', msg=msg)


# Login
@app.route('/')
def home():
    check_sql = f'''SELECT id, color_id, picture, product.title, product.price, color_id
                FROM product, product_has_color where count>0 
                and product_has_color.product_id = product.id group by product.title'''
    products = execute_read_query(connect_db, check_sql)
    print(session)
    # if session.get('logged_in'):
    #     session_login = session['logged_in']
    #     return render_template('home.html', products=products, sess_login=session['logged_in'])
    return render_template('home.html', products=products, sess_login=session)


@app.route("/product/<int:id>/<int:color_id>", methods=['GET', 'POST'])
def product(id, color_id):
    product_in_order = None
    msg = ''
    check_info_product = f'''Select * from type, product, color, product_has_color, product_has_material, material
                        Where product.count>0 and type.id=product.type_id and product.id=product_has_color.product_id 
                        and color.id=product_has_color.color_id and product_has_material.material_id = material.id
                        and product_has_material.product_id = product.id and product.id="{id}" and color_id = "{color_id}"'''
    product_data = execute_read_query(connect_db, check_info_product)
    if product_data == tuple():
        return '<h1>Invalid link</h1>'
    else:
        product_data = product_data[0]

    print(product_data)
    check_picture_product = f'''Select product.id, color.id as color_id, picture from type, product, color, product_has_color
                            Where product.id=product_has_color.product_id 
                            and color.id=product_has_color.color_id
                            and product.id={id}'''
    product_picture = execute_read_query(connect_db, check_picture_product)
    print(product_picture)
    if session.get('logged_in'):
        check_actual_order = f'''SELECT id, actual FROM sofa_shop.order 
                                                    where idUser = {session.get('user_id')} and actual = 1'''
        actual_order = execute_read_query(connect_db, check_actual_order)
        if actual_order != tuple():  # ORDER СУЩЕВСТВУЕТ

            actual_order = actual_order[0]
            id_actual_order = actual_order['id']
            check_product_in_order = f'''select * from order_product where idOrder = {id_actual_order}
                                     and idProduct = {id} and color_id = {color_id}'''
            product_add_order = execute_read_query(connect_db, check_product_in_order)
            if product_add_order != tuple():
                product_in_order = True
                msg = 'Товар добавлен в корзину'
        if request.method == 'POST':
            if actual_order == tuple():  # ORDER НЕ СУЩЕВСТВУЕТ

                print('Order неактуален')
                create_order = f'''INSERT INTO `sofa_shop`.`order` (`idUser`, `datetime`, `actual`)
                               VALUES ('{session.get('user_id')}', curdate(), 1)'''
                id_actual_order = execute_query(connect_db, create_order)
                print(f"{id_actual_order} Order создан")
            check_product_in_order = f'''select * from order_product where idOrder = {id_actual_order}
                                     and idProduct = {id} and color_id = {color_id}'''
            product_add_order = execute_read_query(connect_db, check_product_in_order)
            if product_add_order == tuple():
                insert_product = f'''INSERT INTO `sofa_shop`.`order_product` (`idOrder`, `idProduct`, `count`, `color_id`)
                                VALUES ('{id_actual_order}', '{id}', '1', '{color_id}');'''
                execute_query(connect_db, insert_product)
                product_in_order = True
                msg = 'Товар добавлен в корзину'

        # if product_add_order != tuple():
        #     msg = 'Товар в корзине'

        # msg = 'Товар добавлен в корзину'
        # print(msg)
        # try:
        #     pass
        # except:
        #     pass
        #     msg = 'Возникли неполадки на сервере, повторите позже'
        print(product_in_order)
    return render_template('product.html', pro_item=product_data, pro_pic=product_picture,
                           sess_login=session, msg=msg, product_in_order=product_in_order,
                           color_id=color_id)


@app.route("/cart")
def cart():
    msg = ''
    if session.get('logged_in'):
        check_actual_order = f'''SELECT id FROM sofa_shop.order 
                            where idUser = {session.get('user_id')} and actual = 1'''
        actual_order = execute_read_query(connect_db, check_actual_order)
        if actual_order != tuple():
            id_actual = actual_order[0]['id']
            check_products_cart = f'''SELECT * FROM order_product, product_has_color, product, color
                                Where idOrder = {id_actual} 
                                and order_product.color_id = color.id and product_has_color.color_id = color.id 
                                and idProduct=product.id and product_id=product.id'''
            products_in_cart = execute_read_query(connect_db, check_products_cart)
            check_total_price = f'''SELECT sum(order_product.count*price) as total_price FROM sofa_shop.order_product, product 
                            where idOrder = '{id_actual}' and idProduct=product.id'''
            total_price = str(execute_read_query(connect_db, check_total_price)[0]['total_price']) + ' ₽'
            print(total_price)
            check_total_count = f'''SELECT sum(order_product.count) as total_count FROM sofa_shop.order_product 
                                        where idOrder="{id_actual}"'''
            total_count = execute_read_query(connect_db, check_total_count)[0]['total_count']
            if products_in_cart != tuple():
                return render_template('cart.html', msg=msg, products_in_cart=products_in_cart,
                                       total_count=total_count,
                                       sess_login=session,
                                       total_price=total_price)
        else:
            msg = "Корзина пуста"
    return render_template('cart.html', msg=msg, sess_login=session)

@app.route('/change_count')
def change_count():
    check_actual_order = f'''SELECT id FROM sofa_shop.order 
                                where idUser = {session.get('user_id')} and actual = 1'''
    actual_order = execute_read_query(connect_db, check_actual_order)[0]['id']
    product_id = request.args.get('product_id')
    color_id = request.args.get('color_id')
    product_count = request.args.get('pro_count')

    update_count_product = f'''UPDATE order_product SET `count` = '{product_count}'
    WHERE (`idOrder` = '{actual_order}') and (`idProduct` = '{product_id}') and (`color_id` = '{color_id}');'''
    execute_query(connect_db, update_count_product)

    check_total_price = f'''SELECT sum(order_product.count*price) as total_price FROM sofa_shop.order_product, product 
                                where idOrder = '{actual_order}' and idProduct=product.id'''
    total_price = str(execute_read_query(connect_db, check_total_price)[0]['total_price']) + ' ₽'

    check_total_count = f'''SELECT sum(order_product.count) as total_count FROM sofa_shop.order_product 
                                            where idOrder="{actual_order}"'''
    total_count = f"Товары ({(execute_read_query(connect_db, check_total_count)[0]['total_count'])})"

    return json.dumps({'total_price': total_price, 'total_count': total_count})


@app.route("/cart/delete_product/<int:product_id>/<int:color_id>")
def delete_product(product_id, color_id):
    check_actual_order = f'''SELECT id FROM sofa_shop.order 
                                    where idUser = {session.get('user_id')} and actual = 1'''
    actual_order = execute_read_query(connect_db, check_actual_order)[0]['id']

    delete_product_cart = f'''DELETE FROM `order_product` 
    WHERE (`idOrder` = '{actual_order}') and (`idProduct` = '{product_id}') and (`color_id` = '{color_id}');'''
    execute_query(connect_db, delete_product_cart)

    check_empty_order = f'''SELECT * FROM sofa_shop.order_product where idOrder = {actual_order}'''
    empty_order = execute_read_query(connect_db, check_empty_order)

    if empty_order == tuple():
        drop_order = f'''DELETE FROM `sofa_shop`.`order` WHERE (`id` = '{actual_order}');'''
        execute_query(connect_db, drop_order)
    return redirect(url_for('cart'))

@app.route('/cart_clear')
def cart_clear():
    pass


@app.route("/exit")
def exit_account():
    session.clear()
    session['request'] = request.referrer
    return redirect(session.get('request'))


@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        msg = request.form.get("todo")
        print(msg)
        return jsonify({'msg': msg})
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)
