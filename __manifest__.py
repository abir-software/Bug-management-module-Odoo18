# -*- coding: utf-8 -*-
{
    'name': "Bug Management Module",
    'summary': "Enterprise QA Bug Tracking, 3D Kanban, Bulk Assignment, Dashboard, Analytics",
    'description': """
        Next-level QA Bug Management for Odoo 18: animated kanban, stylish dashboards, bulk assignment wizard, analytics.
        Designed for QA, Developers, and Management teams.
    """,
    'version': '18.0.1.0.0',
    'category': 'Quality',
    'license': 'LGPL-3',
    'author': "Md Abir Hassan",
    'website': "https://www.linkedin.com/in/abirhassan2/",
    'depends': [
        'base',
        'project',
        'web',
        'mail',
        'board',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/management_bug_security.xml',
        'data/bugs_data.xml',
        'views/menu.xml',
        'views/management_bug.xml',
        'views/dashboard.xml',
        'wizard/bug_bulk_assign_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'static/description/icon.png',
            'Bug-management-module-Odoo18/static/src/css/bug_management.css',
        ],
    },
    'images': [
        'static/description/screenshot_management_bug.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
