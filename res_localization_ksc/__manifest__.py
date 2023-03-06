

{
    'name': 'Res Localization Ksc',
    'version': '1.6',
    'category': 'Localization',
    'sequence': 100,
    'summary': 'This Is Res Localization',
    'description': "",
    'website': '',
    'depends': ['base'],
    'data':[
        "security/ir.model.access.csv",
        "views/country_ksc.xml",
        "views/city_ksc.xml",
        "views/state_ksc.xml",
        "reports/res_state_report.xml",
        "reports/res_state_report_template.xml",
        "wizard/state_report_view.xml",

    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
