from flask import render_template, request, session, redirect, url_for
from database.extension import execute_read_query, execute_query


def admin():
    if session.get('admin') != 1:
        return redirect('/')
    return render_template('admin.html')
