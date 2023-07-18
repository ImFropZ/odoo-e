# -*- coding: utf-8 -*-
{
    'name' : 'Web School Layout Customized',
    'version' : '0.1.0',
    'summary': 'Web School Layout Customized',
    'sequence': 1,
    'description': """Web School Layout Customized""",
    'category': 'Website',
    'depends' : ['base', 'web'],
    'data': [
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'assets': {
        'web.assets_backend': [
            'web_school_customized/static/src/webclient/*/*.js',
            'web_school_customized/static/src/webclient/*/*.xml',
            'web_school_customized/static/src/webclient/*/*.scss',
        ],
    },
}