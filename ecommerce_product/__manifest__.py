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
    'version': '16.0.0.2',
    'license': 'LGPL-3',

    'depends': ['base', 'website_sale', 'product', 'website'],

    'data': [
        'security/ir.model.access.csv',
        'views/odoo/product_template_form_view_custom.xml',
        'views/odoo/product_attribute_view_form_custom.xml',
        # 'views/odoo/product_template_only_form_view_custom.xml',
        'views/odoo/product_normal_form_view_custom.xml',
        'views/odoo/fiber_family_view.xml',
        'views/odoo/color_group_view.xml',
        'views/odoo/properties_view.xml',
        'views/odoo/usage_view.xml',
        'views/odoo/product_type_view.xml',
        'views/odoo/structure_view.xml',
        'views/odoo/care_instructions_view.xml',
        'views/odoo/certification_view.xml',
        'views/odoo/available_meters_view.xml',
        'views/odoo/menuitem_product.xml',
        'views/website/product_custom.xml',
        'views/website/attributes_filter_view.xml',
        'views/website/footer_custom_custom.xml',
        'views/website/products_item_custom.xml',
        'views/website/products_custom.xml',
    ],
    'demo': [
    ],
    'assets': {
        'web.assets_backend': [
            'https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap'
        ],
        'web.assets_frontend': [
            # 'ecommerce_product/static/src/scss/foundation.min.css',
            # 'ecommerce_product/static/src/js/foundation.min.js',
            'https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap',
            'ecommerce_product/static/src/scss/style.css',
            'ecommerce_product/static/src/scss/material.min.css',
            'ecommerce_product/static/src/js/material.min.js',
        ]

    }
}
