# -*- coding: utf-8 -*-
{
    'name': "Product Product Info",

    'summary': """Añade pestaña en variantes de producto llamada Ecommerce""",

    'description': """ Añade una pestaña nueva llamada Ecommerce dentro de un producto en las variantes de producto. Muestra información sobre fiber family, property, usage y certifications.
    """,

    'author': "NextaDS",
    'website': "https://nextads.es/",
    'category': 'Product Product',
    'version': '16.0.0.1',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'stock',
        'product'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/certifications_view.xml',
        'views/fiber_family_view.xml',
        'views/properties_view.xml',
        'views/usage_view.xml',
        'views/menuitem_product.xml',
        'views/product_product_custom.xml',
        'views/product_attribute_view.xml',
        'views/color_group_view.xml',
        'views/attributes_variants_view.xml'
    ],
}
