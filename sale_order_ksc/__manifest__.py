# -*- coding: utf-8 -*-


{
    'name': 'sale_order',
    'version': '1.6',
    'sequence': 15,
    'description': "",
    'website': 'https://www.odoo.com/app/sale_order',
    'depends': ['base','sale'],
    'data': [
        "security/ir.model.access.csv",
        "views/sale_order_view_ksc.xml"
    ],
    'demo': [
             ],

    'installable': True,
    'application': True,
    'auto_install': False,

}
