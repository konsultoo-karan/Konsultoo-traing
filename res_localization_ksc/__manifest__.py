{
    'name': 'Localization information & Data',
    'version': '0.15.0.0',
    'summary': 'Localization data',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_country_ksc_views.xml',
        'views/res_state_ksc_views.xml',
        'views/res_city_ksc_views.xml',
        'report/res_country_ksc_report.xml',
        'report/res_country_ksc_template.xml',
        'wizard/countries_report_views.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'

}