from flask import render_template, request, session, redirect, url_for
from database.extension import execute_read_query, execute_query


def admin_panel():

    return render_template('admin_panel.html')
