# Wizard for bulk assigning bugs placeholder
from odoo import models, fields, api

class BugBulkAssign(models.TransientModel):
    _name = 'bug.bulk.assign'
    _description = 'Bulk Assign Bugs'

    user_id = fields.Many2one('res.users', string='Assign to User')
    bug_ids = fields.Many2many('management.bug', string='Bugs')

    def action_assign(self):
        for bug in self.bug_ids:
            bug.write({'user_id': self.user_id.id})
