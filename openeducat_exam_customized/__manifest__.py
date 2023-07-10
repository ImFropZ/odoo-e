# -*- coding: utf-8 -*-
{
    'name': 'Openeducat Exam Customized',
    'version': '1.0.0',
    'sequence': 126,
    'summary': 'Openeducat Exam Customized',
    'author': 'Anakut Digital',
    'category': 'Education/Anakut',
    'description': """
Openeducat Exam Customized by ANAKUT
==========================================

Add
* Group
    * Teacher
        * 

""",
    'depends': [
        'openeducat_classroom',
        'openeducat_exam'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/exam_session_view.xml',

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
