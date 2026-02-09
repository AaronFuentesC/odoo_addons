{
    'name': "gestor_multas",

    'summary': "Gestor de multas desarrollado por Aarón Fuentes Casanova",

    'description': """
Gestor de multa desarrollado por Aarón Fuentes Casanova para el módulo de Sistemas de Gestión Empresarial de 2ºDAM
Para el proyecto de herencia.
    """,

    'author': "Aarón Fuentes Casanova",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr','web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/multa_views.xml',
        'views/tipo_multa_views.xml',
        'views/menu.xml',
        'views/hr_employee_views.xml',
        'reports/report_multas.xml',
        'reports/report_multas_action.xml',
        'reports/report_multa_ficha.xml',
        'reports/report_multa_ficha_action.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

