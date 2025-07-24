from odoo import http
from odoo.http import request

class BugManagementController(http.Controller):
    
    @http.route('/bug_management/dashboard', type='http', auth='user')
    def bug_dashboard(self):
        bugs = request.env['bug.management.bug'].search([])
        values = {
            'bugs': bugs,
            'bug_count': len(bugs),
        }
        return request.render('bug_management_module.bug_dashboard_template', values)