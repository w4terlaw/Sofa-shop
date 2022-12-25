from flask import render_template, request, session, redirect, flash
from database.extension import execute_read_query, execute_query


def admin():
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
        return redirect('/admin')
    return render_template('admin.html', color=all_color, material=all_material)
