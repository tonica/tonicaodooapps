{
    'name': 'Lens Memoria',
    'version': '19.0.1.0.0',
    'summary': 'Gestiona fons fotogràfics (fotos) per Odoo 19 Community',
    'description': 'Module per gestionar fons fotogràfics/col·leccions de fotos associades a fons de càmera o objectes Lens.',
    'category': 'Tools',
    'author': 'OpenCode',
    'website': '',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/lens_memory_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
