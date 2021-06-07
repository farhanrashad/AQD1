# -*- coding: utf-8 -*-

{
    "name": "Crm Item Menu Product",
    'version': '14.0.0.0',
    "category": 'Crm Customization',
    "summary": ' Add Item Menu under the sale as a Product into CRM',
    'sequence': 2,
    "description": """" Add item Menu under the sale as a Product into CRM """,
    "author": "Dynexcel",
    "website": "http://www.dynexcel.co",
    'license': 'LGPL-3',
    'depends': ['base','crm','stock'],
    'data': [

        'views/crm_menu_item_products.xml',
    ],

    "installable": True,
    "application": True,
    "auto_install": False,
}

