from odoo import models, fields, api, _

class BugBulkAssign(models.TransientModel):
    _name = 'bug.bulk.assign'
    _description = 'Bulk Assign Bugs'

    bug_ids = fields.Many2many('bug.management', string="Bugs to Assign")
    user_id = fields.Many2one('res.users', string="Assign to User", required=True)

    def action_assign_bugs(self):
        for bug in self.bug_ids:
            bug.write({
                'assigned_to_id': self.user_id.id,
                'state': 'assigned'
            })
            bug.message_post(body=_("Assigned in bulk to %s" % self.user_id.name))
        return {'type': 'ir.actions.act_window_close'}
