{
    'name': 'Dealer information',
    'version': '15.0.1.1.0',
    'summary': 'dealer information summary',
    'description': """Helps to show dealer information""",
    'category': 'Human Resources',
    'depends': ['base','base_address_city'],
    'data': [
        'security/ir.model.access.csv',
        'views/dealer_information.xml',
        'views/regestration_information.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
