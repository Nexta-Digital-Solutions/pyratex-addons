# -*- coding: utf-8 -*-
{
    'name': "Product Product Info",

    'summary': """Añade pestaña en variantes de producto llamada Ecommerce""",

    'description': """ Añade una pestaña nueva llamada Ecommerce dentro de un producto en las variantes de producto. Muestra información sobre fiber family, property, usage y certifications.
    """,

    'author': "NextaDS",
    'website': "https://nextads.es/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product Product',
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
        'views/certifications_view.xml',
        'views/fiber_family_view.xml',
        'views/properties_view.xml',
        'views/usage_view.xml',
        'views/menuitem_product.xml',
        'views/product_product_custom.xml',
        'views/product_attribute_view.xml',
        'views/color_group_view.xml'
    ],
}
