# -*- coding: utf-8 -*-
{
    "name": "res_localization",
    "version": "1.0.0",
    "category": "",
    'summary': 'Manage localization data',
    'sequence': -100,
    "description": """Preset to create journal localization model  
   Description of the module. 
    """,
    "price": 000,
    "currency": 'EUR',
    "depends": ['base'],
    "data": [
        "security/ir.model.access.csv",
        "views/res_country_views.xml",
        "views/res_state_views.xml",
        "views/res_city_views.xml",
        "report/state_report_template_view.xml",
        "report/state_report_view.xml",
        "wizard/res_state_report.xml"
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
    "license": 'LGPL-3',
}
