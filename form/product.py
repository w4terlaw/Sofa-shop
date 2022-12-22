from flask import render_template, request, session
from database.extension import execute_read_query, execute_query


# PRODUCT PAGE
def product_info(id, color_id):
    product_in_order = None
    msg = ''
    # check_info_product = f'''Select *, GROUP_CONCAT(material SEPARATOR ', ') as full_material, product.id as pro_id from type, product, color, product_has_color, product_has_material, material
    #                        Where product.count>0 and type.id=product.type_id and product.id=product_has_color.product_id
    #                        and color.id=product_has_color.color_id and product_has_material.material_id = material.id
    #                        and product_has_material.product_id = product.id and product.id={id} and color_id = {color_id}'''
    check_info_product = f'''Select *, GROUP_CONCAT(material SEPARATOR ', ') as full_material, product.id as pro_id 
from type, product, product_has_material, material, color, product_has_color
Where product.count>0 and type.id=product.type_id and product_has_material.material_id = material.id
and product.id=product_has_color.product_id
and color.id=product_has_color.color_id
and product_has_material.product_id = product.id and product.id={id} and color_id = {color_id}'''
    product_data = execute_read_query(check_info_product)
    product_data = product_data[0]
    print(product_data)
    check_all_picture_product = f'''Select all_picture.picture  from type, product, color, product_has_color, all_picture
                        Where product.count>0 and type.id=product.type_id and product.id=product_has_color.product_id
                        and color.id=product_has_color.color_id and product.id={id} and color_id = {color_id} and all_picture.product_has_color_id = product_has_color.id'''
    all_picture = execute_read_query(check_all_picture_product)
    print(all_picture)

    check_picture_product = f'''Select product.id, color.id as color_id, picture, picture2 from type, product, color, product_has_color
                            Where product.id=product_has_color.product_id 
                            and color.id=product_has_color.color_id
                            and product.id={id} group by color.id'''
    product_picture = execute_read_query(check_picture_product)
    # print(product_picture)
    if session.get('logged_in'):
        check_actual_order = f'''SELECT id, actual FROM orders
                                                    where idUser = {session.get('user_id')} and actual = 1'''
        actual_order = execute_read_query(check_actual_order)
        if actual_order != tuple():  # ORDER СУЩЕВСТВУЕТ

            actual_order = actual_order[0]
            id_actual_order = actual_order['id']
            check_product_in_order = f'''select * from order_product where idOrder = {id_actual_order}
                                     and idProduct = {id} and color_id = {color_id}'''
            product_add_order = execute_read_query(check_product_in_order)
            if product_add_order != tuple():
                product_in_order = True
                msg = 'Товар добавлен в корзину'
        if request.method == 'POST':
            if actual_order == tuple():  # ORDER НЕ СУЩЕВСТВУЕТ
                create_order = f'''INSERT INTO `orders` (`idUser`, `datetime`, `actual`)
                               VALUES ('{session.get('user_id')}', curdate(), 1)'''
                id_actual_order = execute_query(create_order)
            check_product_in_order = f'''select * from order_product where idOrder = {id_actual_order}
                                     and idProduct = {id} and color_id = {color_id}'''
            product_add_order = execute_read_query(check_product_in_order)
            if product_add_order == tuple():
                insert_product = f'''INSERT INTO `order_product` (`idOrder`, `idProduct`, `count`, `color_id`)
                                VALUES ('{id_actual_order}', '{id}', '1', '{color_id}');'''
                execute_query(insert_product)
                product_in_order = True
                check_total_count = f'''SELECT sum(order_product.count) as total_count FROM order_product 
                                                            where idOrder="{id_actual_order}"'''
                total_count = execute_read_query(check_total_count)[0]['total_count']
                session['count_product_cart'] = total_count
                msg = 'Товар добавлен в корзину'
    return render_template('product.html', pro_item=product_data, all_picture=all_picture, pro_pic=product_picture,
                           msg=msg, product_in_order=product_in_order, color_id=color_id)
