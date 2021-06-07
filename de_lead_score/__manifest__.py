# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name": "CRM Lead Score",
    "category": 'CRM',
    "summary": 'Lead Score',
    "description": """
        this module enable to score leads
    """,
    "sequence": 2,
    "web_icon": "",
    "author": "Dynexcel",
    "website": "www.dynexcel.com",
    "version": '14.0.0.0',
    "depends": ['base','crm',],
    "data": [
        'security/ir.model.access.csv',
        'views/crm_lead_score_views.xml',
        'views/crm_lead_type_views.xml',
        'views/crm_lead_views.xml', 
    ],

    "price": 25,
    "currency": 'EUR',
    "installable": True,
    "application": True,
    "auto_install": False,
}






