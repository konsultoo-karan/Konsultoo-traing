# -*- coding: utf-8 -*-

{
    'name': 'Sale Order Inherit',
    'version': '1.6',
    'category': '',
    'sequence': 15,
    'summary': 'Add New field',
    'description': "",
    'website': 'https://www.odoo.com/app/sale_order_task',
    'depends': ['base','sale'],
    'data':[
        "views/sale_order_inherit.xml",

    ],


    'installable': True,
    'application': True,
    'auto_install': False,

}