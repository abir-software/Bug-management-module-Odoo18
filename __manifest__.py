{
    'name': 'Bug Management Module',
    'version': '1.0',
    'summary': 'Track and manage bugs across software projects',
    'description': """
        A complete bug lifecycle module for tracking, assigning, and resolving bugs.
        Features include:
        - Create and assign bugs
        - Dashboard views
        - Bulk assign functionality
        - Status tracking
        - Severity classification
    """,
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'category': 'Project',
    'depends': ['base', 'mail', 'web'],
    'data': [
        'security/management_bug_security.xml',
        'security/ir.model.access.csv',
        'data/bugs_data.xml',
        'views/menu.xml',
        'views/management_bug.xml',
        'views/dashboard.xml',
        'views/templates.xml',
        'wizard/bug_bulk_assign_view.xml',
        'views/assets.xml',
    ],
    'demo': [
        'data/bugs_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'bug_management_module/static/src/css/bug_management.css',
            'bug_management_module/static/src/js/bug_management.js',
        ],
    },
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}