from flask import request, render_template, session
from database.extension import execute_read_query


# SEARCH PRODUCT
def search():
    if request.args.get('text'):
        value = request.args.get('text')
        check_sql = f'''SELECT id, color_id, picture, product.title, product.price, color_id 
                        FROM product, product_has_color where count>0 
                        and product_has_color.product_id = product.id and product.title LIKE '%{value}%' group by id'''
        products = execute_read_query(check_sql)
        session['search_pro_count'] = len(products)
        return render_template('search.html', search_value=value, products=products)
