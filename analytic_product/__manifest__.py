# -*- coding: utf-8 -*-
{
    'name': "Analytic Product",

    'summary': """
        Analytics for Products""",

    'description': """
         Analytics for Products
    """,

    'author': "NextaDS",
    'website': "https://nextads.es/",

    'category': 'Accounting',
    'version': '16.0.0.1',

    'depends': [
        'purchase',
        'sale_management',
        'account',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/product_template_analytic.xml',
        'data/cron.xml',
    ],
}
