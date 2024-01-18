# -*- coding: utf-8 -*-
{
    'name': "Ecommerce Product",

    'summary': """
        Muestra las características de los productos""",

    'description': """
         Muestra las características de los productos
    """,

    'author': "NextaDS",
    'website': "https://nextads.es/",

    'category': 'Ecommerce',
    'version': '16.0.0.1',
    'license': 'LGPL-3',

    'depends': ['base', 'website_sale', 'product'],

    'data': [
        'views/product_properties_view_custom.xml',
        'views/product_template_form_view_custom.xml',
        'views/product_attribute_view_form_custom.xml',
        'views/product_template_form_view_nds.xml',
        'views/filter_products_price_custom.xml',
        'views/attributes_filter_view.xml'
    ],
    'demo': [
    ],
}
