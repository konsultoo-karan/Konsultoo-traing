{
    'name': 'country Information 2',
    'version': '15.0.1.1.0',
    'summary': 'country  information',
    'description': """Helps to show Customer information""",
    'category': 'Human Resources',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'reports/state_report.xml',
        'reports/state_template_report.xml',
        # 'reports/state_report_wizard.xml',
        'views/res_country_demo2.xml',
        'views/res_state_ksc.xml',
        'views/res_city_view.xml',
        "wizard/state_wizard.xml",
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
