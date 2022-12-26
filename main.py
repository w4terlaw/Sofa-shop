from flask import Flask, jsonify, make_response
from database.extension import mysql
# import datetime
from form import home, cart, search, product, auth, admin, profile

app = Flask(__name__)

app.secret_key = 'XMGriU67zMwuqf7s2lsxlv2cH4QaDGUt'


# app.permanent_session_lifetime = datetime.timedelta(seconds=600)


# Connect DB
def create_connection(host, user, password, db):
    app.config['MYSQL_HOST'] = host
    app.config['MYSQL_USER'] = user
    app.config['MYSQL_PASSWORD'] = password
    app.config['MYSQL_DB'] = db
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    print("Connection to MySQL DB successful")


create_connection('localhost', 'root', 'root', 'sofa_shop')
# create_connection('waterlaw1.mysql.pythonanywhere-services.com', 'waterlaw1', 'elmir2022', 'waterlaw1$sofa_shop')

mysql.init_app(app)

# AUTH
app.add_url_rule('/login', methods=['GET', 'POST'], view_func=auth.login)
app.add_url_rule('/reg', methods=['GET', 'POST'], view_func=auth.reg)
app.add_url_rule('/exit', view_func=auth.exit_account)

# HOME
app.add_url_rule('/', view_func=home.home)
app.add_url_rule('/home', view_func=home.home)


# PRODUCT
app.add_url_rule('/product/<int:id>/<int:color_id>', methods=['GET', 'POST'], view_func=product.product_info)

# CART
app.add_url_rule('/cart', methods=['GET', 'POST'], view_func=cart.cart)
app.add_url_rule('/change_count', view_func=cart.change_count)
app.add_url_rule('/cart_clear', view_func=cart.cart_clear)

# SEARCH
app.add_url_rule('/search/', view_func=search.search)

# ADMIN PANEL
app.add_url_rule('/admin', methods=['GET', 'POST'], view_func=admin.admin)
app.add_url_rule('/admin/add_product', methods=['GET', 'POST'], view_func=admin.add_product)
app.add_url_rule('/admin/red_product/<int:id>', methods=['GET', 'POST'], view_func=admin.red_product)
app.add_url_rule('/admin/del_product/<int:id>', methods=['GET', 'POST'], view_func=admin.del_product)
app.add_url_rule('/del_color/<int:id>/<int:color_id>', methods=['GET', 'POST'], view_func=admin.del_color)
app.add_url_rule('/add_color/<int:id>', methods=['GET', 'POST'], view_func=admin.add_color)
# app.add_url_rule('/admin/redact', view_func=admin_panel.search)
# app.add_url_rule('/admin/del/<int:product_id>', view_func=admin_panel.search)
# app.add_url_rule('/admin/add', view_func=admin_panel.search)

# PROFILE
app.add_url_rule('/profile', methods=['GET', 'POST'], view_func=profile.profile)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
