# -*- coding: utf-8 -*-
{
    'name': "Ecommerce Filter",

    'summary': """Desplazar las categorias del ecommerce a la izquierda
        """,

    'description': """Desplazar las categorias del ecommerce a la izquierda
    """,

    'author': "NextaDS",
    'website': "https://nextads.es/",

    'category': 'Ecommerce',
    'version': '16.0.0.1',
    'license': 'LGPL-3',

    'depends': ['base', 'website_sale'],

    'data': [
        'views/filmstrip_categories_category_views.xml',
        'views/portrait_categories_views.xml',
        'views/products_attributes_add_categories_views.xml',
        'views/attributes_views.xml'
    ],
    'assets':{
        'web.assets_frontend':[
            'ecommerce_filter/static/src/scss/style.css',
            'ecommerce_filter/static/src/scss/foundation.min.css',
        ]
    }
}
