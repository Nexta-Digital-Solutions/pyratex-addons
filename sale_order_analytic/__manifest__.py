# -*- coding: utf-8 -*-
{
    'name': "Sale Order Analytic",

    'summary': """
        Crea una cuenta analitica al confirmar el pedido de venta""",

    'description': """
         Crea una cuenta analitica al confirmar el pedido de venta
    """,

    'author': "NextaDS",
    'website': "https://nextads.es/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'sale_purchase',
        'account',
    ],

    # always loaded
    'data': [
    ],
}
