# -*- coding: utf-8 -*-


{
    'name': 'res_localization_ksc',
    'version': '1.6',
    'sequence': 15,
    'description': "",
    'website': 'https://www.odoo.com/app/res_localization_ksc',
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "views/res_country_ksc_view.xml",
        "views/res_state_ksc_view.xml",
        "views/res_city_ksc_view.xml",
        "report/state_view_report.xml",
        "report/state_view_template.xml",
        "wizard/state_report_view.xml",
    ],
    'demo': [
             ],

    'installable': True,
    'application': True,
    'auto_install': False,

}
