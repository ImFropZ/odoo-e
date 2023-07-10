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
        'openeducat_assignment'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/assignment_view.xml',
        'views/assignment_sub_line_view.xml',

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
