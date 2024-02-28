# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Bizople Solutions Pvt. Ltd.
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Multi Product Publish/Unpublish',
    'category': 'Website',
    'version': '16.0.0.0',
    'author': 'Bizople Solutions Pvt. Ltd.',
    'website': 'https://www.bizople.com',
    'summary': 'Multi Product Publish and Unpublish',
    'description': """Multi Product Publish and Unpublish""",
    'depends': [
        'product',
        'website_sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        
        'wizard/product_publish_view.xml',
    ],
     'images': [
        'static/description/banner.png'
    ],
    'sequence': 1,
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
