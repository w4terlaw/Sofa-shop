from flask import Flask, render_template, request, redirect, url_for, session, jsonify, json
from flask_mysqldb import MySQL, MySQLdb
import re
import datetime
from passlib.hash import sha256_crypt

from db_CRUT import execute_read_query, execute_query

app = Flask(__name__)

app.secret_key = 'super secret key'
app.permanent_session_lifetime = datetime.timedelta(seconds=20)
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
        print(session['request'])
        print(request.referrer)
    # if session.get['refferer_back'] == None:
    #     session['refferer_back'] = True
    # if session['refferer_back']:
    #     session['request'] = request.referrer

    print(session.get('request'))
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']

        check_sql = f'''select * from user where email = "{email}"'''
        login_user = execute_read_query(connect_db, check_sql)
        # print(login_user)
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
                session['id'] = login_user['id']
                print(f"ревест внутри {session.get('request')}")
                if session['request'] != None:
                    return redirect(session.get('request'))
                return redirect(url_for('home'))
            else:
                msg = 'Неверный никнейм или пароль.'
    return render_template('login.html', msg=msg, sess_login=session.get('logged_in'))


# Login
@app.route('/', methods=['GET', 'POST'])
def home():
    check_sql = f'''SELECT id, picture, product.title, product.price, color_id
    FROM product, product_has_color where count>0 and product_has_color.product_id = product.id group by product.title'''
    products = execute_read_query(connect_db, check_sql)
    print(session)
    # if session.get('logged_in'):
    #     session_login = session['logged_in']
    #     return render_template('home.html', products=products, sess_login=session['logged_in'])
    print("Сессия завершена")
    return render_template('home.html', products=products, sess_login=session.get('logged_in'))


@app.route("/product/<int:id>", methods=['GET', 'POST'])
def product(id):
    msg = ''
    check_sql = f'''select * from type, product, color, product_has_color, product_has_material, material
    where product.count>0
    and type.id=product.type_id
    and product.id=product_has_color.product_id 
    and color.id=product_has_color.color_id 
    and product.id=product_has_material.product_id
    and material.id=product_has_material.material_id 
    and product.id={id} group by product.title'''
    product_data = execute_read_query(connect_db, check_sql)[0]
    # print(product_data)

    return render_template('product.html', pro_item=product_data, sess_login=session.get('logged_in'))


#
# # Create lesson
# @app.route('/create_lesson', methods=['GET', 'POST'])
# def create_lessons():
#     if request.method == 'POST':
#         title_lesson = request.form['title_lesson']
#
#         check_sql = f'''insert into lessons (title, user_id) values ('{title_lesson}', {session['id']})'''
#         ID = execute_query(connect_db, check_sql)
#
#         return redirect(url_for('.lessons', id=ID))
#
#     return render_template("create_lesson.html")
#
#
# # show specific lesson and its lists
# @app.route("/lessons/<int:id>", methods=['GET', 'POST'])
# def lessons(id):
#     check_sql = f'''SELECT * FROM lessons WHERE id = {id}'''
#     lesson = execute_read_query(connect_db, check_sql)[0]
#     check_sql = f'''SELECT lists.id, lists.date from lessons, lists where lessons.id = lessons_id AND lessons_id = {id} '''
#     data = execute_read_query(connect_db, check_sql)
#     if request.method == 'POST':
#         check_sql = f'''INSERT INTO `qr_site`.`lists` (`date`, `lessons_id`) VALUES (Curtime(), {id})'''
#         execute_query(connect_db, check_sql)
#
#         return redirect(url_for('lessons', id=id))
#
#     return render_template('lesson.html', lesson=lesson, lists=data)
#
#
# @app.route("/lessons/<int:id>/<int:id_lists>", methods=['GET', 'POST'])
# def lists(id, id_lists):
#     if not session:
#         return redirect(url_for('login'))
#     check_sql = f'''Select TIMEDIFF(curtime(),(SELECT date_scan FROM lists_has_students WHERE user_id = {session['id']} and lists_id = {id_lists}  ORDER BY date_scan DESC LIMIT 1)) as timediff'''
#     timediff = execute_read_query(connect_db, check_sql)[0]
#     if not session['teacher'] and timediff['timediff'] != None:
#         if timediff['timediff'] > datetime.timedelta(seconds=3000):
#             write_sql = f'''INSERT INTO `qr_site`.`lists_has_students` (`lists_id`, `date_scan`, `user_id`) VALUES ('{id_lists}', CURTIME(), {session["id"]})'''
#             execute_query(connect_db, write_sql)
#     elif not session['teacher']:
#         write_sql = f'''INSERT INTO `qr_site`.`lists_has_students` (`lists_id`, `date_scan`, `user_id`) VALUES ('{id_lists}', CURTIME(), {session["id"]})'''
#         execute_query(connect_db, write_sql)
#
#     check_sql = f'''SELECT * FROM lists WHERE id = {id_lists}'''
#     list_one = execute_read_query(connect_db, check_sql)[0]
#     check_sql = f'''
#     Select CONCAT_WS(' ', first_name, last_name) as student, groupp,
#     group_concat(distinct time(date_scan) SEPARATOR ' - ') as date
#     from lists_has_students, user
#     where lists_id = {id_lists} and user.id = lists_has_students.user_id and user.teacher = 0
#     group by student, groupp'''
#     data_students = execute_read_query(connect_db, check_sql)
#     qr = f'site.com/lessons/{id}/{id_lists}'
#     return render_template('lists.html', list_one=list_one, students=data_students, qr=qr)
#
#
# # Update data from DB
# @app.route("/red/<int:upd_id>", methods=['GET', 'POST'])
# def update_db(upd_id):
#     check_sql = f'''SELECT title FROM lessons WHERE id = {upd_id}'''
#     title_lesson = execute_read_query(connect_db, check_sql)[0]
#
#     if request.method == 'POST':
#         update_lesson = request.form['update_text_lesson']
#
#         check_sql = f'''UPDATE lessons SET `title` = '{update_lesson}' WHERE (`id` = {upd_id});'''
#         execute_query(connect_db, check_sql)
#
#         return redirect(url_for('check_lessons'))
#
#     return render_template('update_lesson.html', title_lesson=title_lesson)
#
#
# # Delete data from DB
# @app.route("/del/<int:del_lesson_id>")
# def delete_lesson_db(del_lesson_id):
#     check_sql = f'''DELETE FROM lessons WHERE (`id` = '{del_lesson_id}')'''
#     execute_query(connect_db, check_sql)
#
#     return redirect(url_for('check_lessons'))
#

@app.route("/exit")
def exit_account():
    session.clear()
    session['request'] = request.referrer
    return redirect(session.get('request'))


@app.route('/test_add', methods=['GET', 'POST'])
def add_to_test():
    name = request.form['name']
    return json.dumps({'msg': name})


@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        msg = request.form.get("todo")
        print(msg)
        return jsonify({'msg': msg})
    return render_template('test.html')


@app.route("/cart")
def cart():
    return 'hello'


#
#
# @app.route("/lessons/<int:id>/del/<int:del_list_id>")
# def delete_list_db(id, del_list_id):
#     check_sql = f'''DELETE FROM lists WHERE (`id` = '{del_list_id}')'''
#     execute_query(connect_db, check_sql)
#
#     return redirect(url_for('.lessons', id=id))


if __name__ == '__main__':
    app.run(debug=True)
