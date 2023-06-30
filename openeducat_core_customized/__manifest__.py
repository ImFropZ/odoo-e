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

Changing

* Faculty Form View
""",
    'depends': ["openeducat_core"],
    'data': [
        'views/faculty_view.xml',
        'views/student_view.xml',
        'views/student_course_view.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': False,
    'assets': {

    },
    'license': 'LGPL-3',
}