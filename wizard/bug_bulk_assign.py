from odoo import models, fields, api, _
from odoo.exceptions import UserError

class BugBulkAssignWizard(models.TransientModel):
    _name = 'bug.bulk.assign.wizard'
    _description = 'Bulk Assign Bugs to User'
    
    user_id = fields.Many2one('res.users', string="Assign To", required=True)
    note = fields.Text(string="Additional Notes")
    
    def action_bulk_assign(self):
        self.ensure_one()
        if not self.user_id:
            raise UserError(_("Please select a user to assign bugs to."))
        
        active_ids = self.env.context.get('active_ids')
        if not active_ids:
            raise UserError(_("No bugs selected. Please select bugs to assign."))
        
        bugs = self.env['bug.management.bug'].browse(active_ids)
        
        # Update bugs
        bugs.write({
            'assigned_to': self.user_id.id,
            'status': 'assigned'
        })
        
        # Add note to chatter
        if self.note:
            for bug in bugs:
                bug.message_post(body=_("Bulk assigned to %s with note: %s") % (self.user_id.name, self.note))
        
        # Return notification
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Success'),
                'message': _('%s bugs have been assigned to %s.') % (len(bugs), self.user_id.name),
                'sticky': False,
                'type': 'success',
                'next': {'type': 'ir.actions.act_window_close'},
            }
        }