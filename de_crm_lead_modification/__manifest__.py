# -*- coding: utf-8 -*-
{
    'name': "CRM Lead Modifications",
    'summary': """
        CRM Lead Modificaiton
        """,
    'description': """
        CRM Lead Modification
    """,
    'author': "Dynexcel",
    'website': "https://www.dynexcel.com",
    'category': 'CRM',
    'version': '14.0.0.1',
    'depends': ['base','crm','sales_team'],
    'data': [
        #'security/ir.model.access.csv',
        'data/lead_data.xml',
        'views/lead_views.xml',
        #'views/lead_search_views.xml',
        #'views/lead_city_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
