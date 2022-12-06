# -*- coding: utf-8 -*-
{
    'name': "VADACTRO-Services",

    'summary': """
        Offer's Personalized Dashboard For VADACTRO Client.
        """,

    'description': """
        Offer's Personalized Dashboard For VADACTRO Client.
    """,

    'author': "Shreyash Tapare",
    'website': "http://www.vadactro.org.in",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        'views/my_account_extension.xml',
        'views/assets.xml'
    ],

    'sequence': -100 ,
    'application': True,
    'license': 'LGPL-3',
}
