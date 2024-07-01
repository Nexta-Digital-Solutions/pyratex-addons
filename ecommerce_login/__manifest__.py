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
    'version': '16.0.0.5',
    'license': 'LGPL-3',

    'depends': [
        'base', 
        'website', 
        'website_sale',
        'documents'
    ],

    'data': [
        'views/complete_your_profile.xml',
        'views/billing_address.xml',
        'views/signup_custom.xml',
        'views/mlnda.xml',
        'views/process_complete.xml'
    ],
    
    'assets': {
        'web.assets_backend': [
            # 'https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap'
        ],
        'web.assets_frontend': [
            'ecommerce_login/static/src/js/vue@2.7.14.js',
            'ecommerce_login/static/src/js/vue_instance.js',
            'ecommerce_login/static/src/scss/signature.scss',
            'ecommerce_login/static/src/js/jquery.serializejson.min.js'
            #'ecommerce_login/static/src/scss/foundation.min.css',
            #'ecommerce_login/static/src/js/foundation.min.js',
            # 'https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap',
        ]

    }
}
