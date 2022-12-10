from flask import render_template, request, session, redirect, url_for
from database.operations import execute_read_query, execute_query
from passlib.hash import sha256_crypt


# REGISTRATION
def reg():
    msg = ''
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = sha256_crypt.encrypt(request.form['password'])

        check_sql = f'''select * from user where email = "{email}"'''
        account = execute_read_query(check_sql)

        if account:
            msg = 'Этот email уже занят.'
        elif first_name[0].islower() or last_name[0].islower():
            msg = 'Имя и фамилия должны начинаться с заглавных букв.'
        elif len(request.form['password']) < 8:
            msg = 'Пароль должен содержать не менее 8 символов.'
        else:
            write_sql = f'''INSERT INTO `user` (`email`, `password`, `first_name`, `last_name`) 
            VALUES ('{email}', '{password}', '{first_name}', '{last_name}')'''
            execute_query(write_sql)
            return redirect(url_for('login'))
    return render_template('registration.html', msg=msg)


# LOGIN
def login():
    # print(request.url_root + 'login')
    if (request.referrer != request.url_root + 'login') and (request.referrer != request.url_root + 'reg'):
        session['request'] = request.referrer
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']

        check_sql = f'''select * from user where email = "{email}"'''
        login_user = execute_read_query(check_sql)
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
                # check_actual_order = f'''SELECT id FROM orders
                #                                     where idUser = {session.get('user_id')} and actual = 1'''
                # actual_order = execute_read_query(connect_db, check_actual_order)[0]['id']
                # check_count_product_cart = f''''''[0]
                # session['count_product_cart'] = check_count_product_cart
                if session.get('request'):
                    return redirect(session.get('request'))
                return redirect(url_for('home'))
            else:
                msg = 'Неверный никнейм или пароль.'
    return render_template('login.html', msg=msg)


# ACCOUNT LOGOUT
def exit_account():
    session.clear()
    session['request'] = request.referrer
    return redirect(session.get('request'))
