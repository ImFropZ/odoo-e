# -*- coding: utf-8 -*-
{
    'name': 'Openeducat Core Customized',
    'version': '1.0.0',
    'sequence': 126,
    'summary': 'Openeducat Core Customized',
    'author': 'Anakut Digital',
    'category': 'Education/Anakut',
    'description': """
Openeducat Core Customized by ANAKUT
=====================================

Add

* Group
    * Teacher
        * Faculty menu
        * Student menu
        * Student Course menu

Changing

* Faculty Form View
* Student Form View
* Student Course Form View

""",
    'depends': ["openeducat_core"],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/faculty_view.xml',
        'views/student_view.xml',
        'views/student_course_view.xml',

        'menu/faculty_menu.xml',
        'menu/student_menu.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': False,
    'assets': {

    },
    'license': 'LGPL-3',
}
