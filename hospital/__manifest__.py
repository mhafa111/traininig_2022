{
    'name': 'Hospital management',
    'version': '15.0.1.0.2',
    'summary': 'Hospital Management',
    'description': """Odoo 15 Development Tutorials""",
    'category': 'Tutorials',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hospital_doctor_views.xml',
        'views/patient_views.xml',
        'views/appointment_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
}
