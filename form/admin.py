from flask import render_template, request, session, redirect, flash, url_for
from database.extension import execute_read_query, execute_query


def admin():
    check_product = f'''SELECT product.id, title, type_title as type, description, price, country, weight, overall, seat 
                        FROM product, type where type.id = product.type_id;'''
    product = execute_read_query(check_product)
    return render_template('admin.html', product=product)


# ADD PRODUCT
def add_product():
    if session.get('admin') != 1:
        return redirect('/')
    check_color = f'''SELECT * FROM color'''
    all_color = execute_read_query(check_color)
    check_material = f'''SELECT * FROM material'''
    all_material = execute_read_query(check_material)
    if request.method == 'POST':
        try:
            overall = f'''{request.form.get('overall_h')} см в высоту, {request.form.get('overall_w')} см в ширину и {request.form.get('overall_d')} см в глубину.'''
            seat = f'''{request.form.get('seat_h')} см в высоту, {request.form.get('seat_w')} см в ширину и {request.form.get('seat_d')} см в глубину. '''
            meterial = request.form.getlist('material')
            insert_new_product = f'''INSERT INTO `product` (`title`, `type_id`, `description`,
            `price`, `count`, `country`, `weight`, `overall`, `seat`) VALUES ('{request.form.get('title')}',
            '{request.form.get('type')}', '{request.form.get('description')}',  '{request.form.get('price')}', 1,
            '{request.form.get('country')}', '{request.form.get('weight')}', '{overall}', '{seat}') '''

            new_product_id = execute_query(insert_new_product)
            for i in range(len(meterial)):
                insert_material_product = f'''INSERT INTO `product_has_material` (`product_id`, `material_id`) 
                VALUES ('{new_product_id}', '{meterial[i]}')'''
                execute_query(insert_material_product)

            insert_color_and_picture = f'''INSERT INTO `product_has_color` (`product_id`, `color_id`, `picture`, `picture2`)
            VALUES ('{new_product_id}', '{request.form.get('color')}', '{request.form.get('picture')}',
             '{request.form.get('picture2')}]');'''
            product_has_color_id = execute_query(insert_color_and_picture)

            all_picture = request.form.get('all_picture').split()
            print(all_picture)
            for i in range(len(all_picture)):
                insert_other_picture = f'''INSERT INTO `all_picture` (`picture`, `product_has_color_id`)
                VALUES ('{all_picture[i]}', '{product_has_color_id}')'''
                execute_query(insert_other_picture)
            flash('Товар добавлен', category='success')
        except Exception as e:
            flash('Произошла ошибка', category='danger')
            print(e)
        return redirect('/admin/add_product')
    return render_template('add_product.html', color=all_color, material=all_material)


# REDACT PRODUCT
def red_product(id):
    check_product = f'''SELECT product.id, title, type_title as type, description, price, country, weight, overall, seat 
                        FROM product, type where type.id = product.type_id and product.id={id}'''
    product = execute_read_query(check_product)[0]

    check_material = f'''SELECT * FROM material'''
    all_material = execute_read_query(check_material)

    active_material = f'''SELECT * FROM product_has_material, material where product_id = {id} 
                            and material.id = material_id'''
    act_material = execute_read_query(active_material)

    check_all_color = f'''SELECT color.id, color.color FROM color where id NOT IN (SELECT color_id FROM product_has_color, color 
                            Where product_id = {id} and color_id=color.id)'''
    all_color = execute_read_query(check_all_color)

    check_color_product = f'''Select product_has_color.id, product.id as product_id, color.id as color_id, color, picture2 
    from type, product, color, product_has_color Where product.id=product_has_color.product_id 
    and color.id=product_has_color.color_id and product.id={id} group by color.id'''
    product_picture = execute_read_query(check_color_product)
    if request.method == 'POST':
        insert_new_product = f'''UPDATE `product` SET `title` = '{request.form.get('title')}', `type_id` = '1',
        `description` = '{request.form.get('description')}', `price` = '{request.form.get('price')}',
        `country` = '{request.form.get('country')}', `weight` = '{request.form.get('weight')}',
        `overall` = '{request.form.get('overall')}',`seat` = '{request.form.get('seat')}' WHERE (`id` = '{id}');
'''
        execute_query(insert_new_product)
        material = request.form.getlist('material')
        del_material = f'''DELETE FROM `product_has_material` WHERE (`product_id` = '{id}')'''
        execute_query(del_material)
        for i in range(len(material)):
            insert_material = f'''INSERT INTO `product_has_material` (`product_id`, `material_id`) 
            VALUES ('{id}', '{material[i]}')'''
            execute_query(insert_material)
        flash('Товар изменён', category='success')
        return redirect(url_for('.red_product', id=id))
    return render_template('red_product.html', product=product, material=all_material, act_material=act_material,
                           pro_pic=product_picture, all_color=all_color)


# ADD COLOR
def add_color(id):
    try:
        insert_new_color = f'''INSERT INTO `product_has_color` (`product_id`, `color_id`, `picture`, `picture2`) 
                        VALUES ('{id}', '{request.form.get('color')}', '{request.form.get('picture')}', '{request.form.get('picture2')}')'''
        id_new_color = execute_query(insert_new_color)
        all_picture = request.form.get('all_picture').split()
        for i in range(len(all_picture)):
            insert_all_pictures = f'''INSERT INTO `all_picture` (`picture`, `product_has_color_id`) 
            VALUES ('{all_picture[i]}', '{id_new_color}');'''
            execute_query(insert_all_pictures)
        flash('Новый цвет добавлен', category='success')
    except Exception as e:
        flash('Произошла ошибка', category='danger')
        print(e)
    return redirect(url_for('.red_product', id=id))


# DEL COLOR
def del_color(id, color_id):
    try:
        del_colors = f'''DELETE FROM product_has_color WHERE product_id = {id} and color_id = {color_id} '''
        execute_query(del_colors)
        flash('Цвет был удалён', category='success')
    except Exception as e:
        flash('Цвет не был удалён', category='danger')
        print(e)
    return redirect(url_for('.red_product', id=id))


# DEL PRODUCT
def del_product(id):
    try:
        dell_product = f'''DELETE FROM `product` WHERE (`id` = '{id}')'''
        execute_query(dell_product)
        flash('Товар успешно удалён', category='success')
    except Exception as e:
        flash('Товар не был удалён', category='danger')
        print(e)
    return redirect(url_for('admin'))
