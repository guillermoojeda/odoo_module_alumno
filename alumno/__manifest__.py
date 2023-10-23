{
    'name': 'Alumno',
    'author': 'Guillermo Ojeda',
    'summary': 'Aplicacion de prueba para ADEN',
    'description': '''
    El resultado de realizar un modulo como prueba tecnica, como parte de la
    entrevista de selección en ADEN
    ''',
    'license': 'LGPL-3',
    'website': 'https://www.linkedin.com/in/guillermo-francsico-ojeda/',
    'depends': [
        'base'
    ],
    'data': [
        'security/guilleApp_security.xml',
        'views/escuela_inscripcion_views.xml',
        # 'data/escuela.alumno.csv',
        # 'views/body_function_views.xml',
        # 'views/body_illness_views.xml',
        # 'views/body_organ_views.xml',
        'views/escuela_alumno_views.xml',
        'views/escuela_programa_views.xml',
        # 'views/body_disease_views.xml',
        'views/menu_item_views.xml',
        'data/escuela.alumno.csv',
        'data/escuela.programa.csv',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
