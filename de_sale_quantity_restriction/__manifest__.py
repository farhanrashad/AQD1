# -*- coding: utf-8 -*-
{
    'name': "Sale Quantity Restriction",
    'version': '14.0.0.0',
    'category': 'sale ',
    'summary': 'This module purpose that It will not allow to show those products that have 0 quantity on (product filter) order/add a product  ',
    'sequence': 3,
    'description': """"  """,
    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",
    'license': 'LGPL-3',
    'depends': ['base','sale'],
    
    'data': [
        
#         'security/ir.model.access.csv',   
           'views/sale_quantity_restriction.xml',
    ],

    "installable": True,
    "application": True,
    "auto_install": False,
}
