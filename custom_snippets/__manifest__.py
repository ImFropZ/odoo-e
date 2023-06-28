# -*- coding: utf-8 -*-
{
    'name': 'Custom Snippets',
    'version': '1.0.0',
    'sequence': 1,
    'summary': 'Anakut eCommerce Snippets',
    'author': 'Testing',
    'category': 'Website/Snippet',
    'description': "",
    'depends': ["website"],
    'data': [
        'security/ir.model.access.csv',

        # Snippet
        'views/snippets/explore-cities.xml',
        'views/snippets/snippets.xml',
        'views/yh_cities.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': False,
    'assets': {
        'web.assets_frontend': [
            'custom_snippets/static/src/js/explore-cities.js',
            'custom_snippets/static/src/js/explore-cities-options.js',
        ],
    },
    'license': 'LGPL-3',
}
