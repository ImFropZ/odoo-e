# -*- coding: utf-8 -*-
{
    'name': 'Openeducat Parent Customized',
    'version': '1.0.0',
    'sequence': 126,
    'summary': 'Openeducat Parent Customized',
    'author': 'Anakut Digital',
    'category': 'Education/Anakut',
    'description': """
Openeducat Parent Customized by ANAKUT
==========================================

Add
* Group
    * Teacher
        * 

""",
    'depends': [
        'openeducat_parent'
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/parent_view.xml',

        'menu/op_menu.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': False,
    'assets': {

    },
    'license': 'LGPL-3',
}
