from flask import render_template, session, redirect, request, flash
from database.extension import execute_read_query, execute_query
from passlib.hash import sha256_crypt


# PROFILE PAGE
def profile():
    if not session.get('logged_in'):
        return redirect('/')
    if request.form.get('password') and request.method == 'POST':
        current_password = request.form['password']
        new_password = request.form['new_password']
        repeat_password = request.form['repeat_password']

        check_sql = f'''select * from user where email = '{session.get('email')}' '''
        login_user = execute_read_query(check_sql)
        if sha256_crypt.verify(current_password, login_user[0]['password']):
            if new_password != repeat_password:
                flash('Пароли не совпадают', category='danger')
                return redirect('/profile')
            new_password = sha256_crypt.encrypt(new_password)
            update_password = f'''UPDATE user` SET `password` = '{new_password}' 
                                    WHERE (`email` = '{session.get('email')}')'''
            execute_query(update_password)
            flash('Пароль успешно изменён', category='success')
            return redirect('/profile')
        else:
            flash('Текущий пароль неверный', category='danger')
            return redirect('/profile')
    if request.form.get('first_name') and request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        address = request.form['address']
        update_profile_data = f'''UPDATE `user` 
        SET `first_name` = '{first_name}', `last_name` = '{last_name}', \
         `address` = '{address}' WHERE (`email` = '{session['email']}') '''
        execute_query(update_profile_data)
        check_updates = f"Select * from user where email = '{session['email']}'"
        user_updates = execute_read_query(check_updates)[0]
        session['first_name'] = user_updates['first_name']
        session['last_name'] = user_updates['last_name']
        session['address'] = user_updates['address']
        return redirect('/profile')
    return render_template('profile.html')
