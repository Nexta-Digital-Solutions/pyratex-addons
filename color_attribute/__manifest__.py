# -*- coding: utf-8 -*-
{
    'name': "Color Attribute",

    'summary': """""",

    'description': """ 
    """,

    'author': "NextaDS",
    'website': "https://nextads.es/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Color attribute',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'stock',
        'product'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_attribute_view.xml',
        'views/color_group_view.xml'
    ],
}
