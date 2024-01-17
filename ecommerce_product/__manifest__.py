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
        'security/ir.model.access.csv',
        'views/product_properties_views.xml',
        'views/product_template_form_view_custom.xml',
        'views/product_attribute_view_form_custom.xml',
        'views/product_template_form_view_nds.xml',
    ],
    'demo': [
    ],
}
