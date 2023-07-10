# -*- coding: utf-8 -*-
{
    'name': 'Openeducat Attendance Customized',
    'version': '1.0.0',
    'sequence': 126,
    'summary': 'Openeducat Attendance Customized',
    'author': 'Anakut Digital',
    'category': 'Education/Anakut',
    'description': """
Openeducat Attendance Customized by ANAKUT
==========================================

Add
* Group
    * Teacher
        * Attendance menu
        * Attendance Submission menu

""",
    'depends': [
        'openeducat_attendance'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/attendance_sheet_view.xml',

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
