# -*- coding: utf-8 -*-
{
    'name': "Escuela",

    'summary': """
        Gestion de Profesores""",

    'description': """
        Gestión de sistema de escuela básica
    """,

    'author': "ADEN",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/escuela_alumno_view.xml',
        'views/escuela_profesor_view.xml',
        'views/escuela_materia_view.xml',
        'views/escuela_inscripcion_view.xml'
    ],
    'installable': True,
    'application': True
}