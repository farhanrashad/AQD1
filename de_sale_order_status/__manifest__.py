# -*- coding: utf-8 -*-
{
    'name': "Sale Order Status",
    'summary': """
    Sale Order Status
        """,
    'description': """
        Sale Order Statuses:-
        - Reserve/Booked
        - Booking Confirmed
        - Booked
    """,
    'author': "Dynexcel",
    'website': "http://www.dynexcel.com",
    'category': 'Sale',
    'version': '14.0.0.1',
    'depends': ['sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/product_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
