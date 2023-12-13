# -*- coding: utf-8 -*-
{
    'name': "Purchase Analytic Account",

    'summary': """
        Add analytic account to purchase and purchase report""",

    'description': """
         Add analytic account to purchase and purchase report
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
