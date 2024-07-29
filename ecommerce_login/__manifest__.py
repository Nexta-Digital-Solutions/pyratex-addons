# -*- coding: utf-8 -*-
{
    'name': "Ecommerce Login",

    'summary': """
        Modificaciones en el login para el acceso y configuración de MNDA.
        """,

    'description': """
        Modificaciones en el login para el acceso y configuración de MNDA.
    """,

    'author': "NextaDS",
    'website': "https://nextads.es/",

    'category': 'Ecommerce',
    'version': '16.0.1.1',
    'license': 'LGPL-3',

    'depends': [
        'base', 
        'website', 
        'website_sale',
        'documents',
        'documents_account'
    ],
    'external_dependencies': {
        'python': ['python-docx'],
    },

    'data': [
        'views/complete_your_profile.xml',
        'views/billing_address.xml',
        'views/signup_custom.xml',
        'views/mlnda.xml',
        'views/process_complete.xml',
        'views/loader.xml' 
    ],
    
    'assets': {
        'web.assets_frontend': [
            'ecommerce_login/static/src/js/vue@2.7.14.js',
            'ecommerce_login/static/src/js/vue_instance.js',
            'ecommerce_login/static/src/scss/signature.scss',
            'ecommerce_login/static/src/js/jquery.serializejson.min.js',
            'ecommerce_login/static/src/scss/loader.scss'
        ]
    }
}
