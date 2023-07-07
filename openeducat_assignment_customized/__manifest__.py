# -*- coding: utf-8 -*-
{
    'name': 'Openeducat Assignment Customized',
    'version': '1.0.0',
    'sequence': 126,
    'summary': 'Openeducat Assignment Customized',
    'author': 'Anakut Digital',
    'category': 'Education/Anakut',
    'description': """
Openeducat Assignment Customized by ANAKUT
==========================================

Add
* Group
    * Teacher
        * Assignment menu
        * Assignment Submission menu

""",
    'depends': [
        'base_automation',
        'openeducat_core',
        'openeducat_core_customized'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        
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
