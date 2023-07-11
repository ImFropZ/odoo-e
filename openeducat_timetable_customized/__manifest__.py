# -*- coding: utf-8 -*-
{
    'name': 'Openeducat Timetable Customized',
    'version': '1.0.0',
    'sequence': 126,
    'summary': 'Openeducat Timetable Customized',
    'author': 'Anakut Digital',
    'category': 'Education/Anakut',
    'description': """
Openeducat Timetable Customized by ANAKUT
==========================================

Add
* Group
    * Teacher
        * 

""",
    'depends': [
        'openeducat_timetable'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/timetable_view.xml',

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
