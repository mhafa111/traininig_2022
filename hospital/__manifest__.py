{
    'name': 'Hospital management',
    'version': '15.0.0.1',
    'summary': 'Hospital Management',
    'description': """Odoo 15 Development Tutorials""",
    'category': 'Tutorials',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_doctor_views.xml',
        'views/hospital_department_views.xml'
    ],
    'demo': ['Department',],
    'installable': True,
    'application': True,
}
