from flask import render_template, request, redirect, session, json, flash
from database.extension import execute_read_query, execute_query


# PRODUCTS CART
# @app.route("/cart")
def cart():
    msg = ''
    if session.get('logged_in'):
        check_actual_order = f'''SELECT id FROM orders
                            where idUser = {session.get('user_id')} and actual = 1'''
        actual_order = execute_read_query(check_actual_order)
        if actual_order != tuple():
            id_actual = actual_order[0]['id']
            if request.method == 'POST':
                if request.form.get('product_id') and request.form['color_id']:
                    delete_product_cart = f'''DELETE FROM `order_product` 
                    WHERE (`idOrder` = '{id_actual}') and (`idProduct` = '{request.form['product_id']}') and (`color_id` = '{request.form['color_id']}');'''
                    execute_query(delete_product_cart)

                    check_empty_order = f'''SELECT * FROM order_product where idOrder = {id_actual}'''
                    empty_order = execute_read_query(check_empty_order)

                    if empty_order == tuple():
                        del session['count_product_cart']
                        execute_query(f'''DELETE FROM `orders` WHERE (`id` = '{id_actual}')''')
                        return redirect('/cart')
            check_products_cart = f'''SELECT * FROM order_product, product_has_color, product, color
                                Where idOrder = {id_actual} 
                                and order_product.color_id = color.id and product_has_color.color_id = color.id 
                                and idProduct=product.id and product_id=product.id group by color.id, product.id'''

            products_in_cart = execute_read_query(check_products_cart)
            check_total_price = f'''SELECT sum(order_product.count*price) as total_price FROM order_product, product 
                            where idOrder = '{id_actual}' and idProduct=product.id'''
            total_price = str(execute_read_query(check_total_price)[0]['total_price']) + ' ₽'
            check_total_count = f'''SELECT sum(order_product.count) as total_count FROM order_product 
                                        where idOrder='{id_actual}' '''
            total_count = execute_read_query(check_total_count)[0]['total_count']
            session['count_product_cart'] = total_count
            if products_in_cart != tuple():
                return render_template('cart.html', msg=msg, products_in_cart=products_in_cart,
                                       total_count=total_count,
                                       total_price=total_price)
        else:
            msg = "Корзина пуста"
    return render_template('cart.html', msg=msg)


# CHANGE COUNT PRODUCT IN CART
# @app.route('/change_count')
def change_count():
    check_actual_order = f'''SELECT id FROM orders
                                where idUser = {session.get('user_id')} and actual = 1'''
    actual_order = execute_read_query(check_actual_order)[0]['id']
    product_id = request.args.get('product_id')
    color_id = request.args.get('color_id')
    product_count = request.args.get('pro_count')
    update_count_product = f'''UPDATE order_product SET `count` = '{product_count}'
    WHERE (`idOrder` = '{actual_order}') and (`idProduct` = '{product_id}') and (`color_id` = '{color_id}');'''
    execute_query(update_count_product)

    check_total_price = f'''SELECT sum(order_product.count*price) as total_price FROM order_product, product 
                                where idOrder = '{actual_order}' and idProduct=product.id'''
    total_price = str(execute_read_query(check_total_price)[0]['total_price']) + ' ₽'

    check_total_count = f'''SELECT sum(order_product.count) as total_count FROM order_product 
                                            where idOrder='{actual_order}' '''
    total_count = execute_read_query(check_total_count)[0]['total_count']
    session['count_product_cart'] = total_count

    # session['count_product_cart'] = total_count
    return json.dumps({'total_price': total_price, 'total_count': total_count})


# CLEAR CART
# @app.route('/cart_clear')
def cart_clear(id):
    del session['count_product_cart']
    execute_query(f'''DELETE FROM `orders` WHERE (`id` = '{id}')''')
    flash('Корзина была очищена', category='info')
    return redirect('/cart')


# PAYMENT CART
def cart_payment(id):
    del session['count_product_cart']
    execute_query(f'''DELETE FROM `orders` WHERE (`id` = '{id}')''')
    flash('Заказ оформлен и оплачен', category='success')
    return redirect('/cart')
