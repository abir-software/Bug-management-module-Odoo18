from odoo import models, fields, api

class BugBulkAssign(models.TransientModel):
    _name = 'bug.bulk.assign'
    _description = 'Bulk Assign Bugs'

    user_id = fields.Many2one('res.users', string='Assign To', required=True)
    bug_ids = fields.Many2many('bug.management', string='Bugs', required=True)

    @api.multi
    def action_assign_bugs(self):
        for bug in self.bug_ids:
            bug.assigned_user_id = self.user_id
        return {'type': 'ir.actions.act_window_close'}