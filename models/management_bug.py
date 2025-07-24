from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class BugManagement(models.Model):
    _name = 'bug.management.bug'
    _description = 'Bug Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'priority desc, create_date desc'

    name = fields.Char(string="Title", required=True, tracking=True)
    description = fields.Html(string="Description")
    severity = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical')
    ], string="Severity", default='medium', tracking=True)
    
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High'),
        ('3', 'Critical')
    ], string="Priority", default='1', tracking=True)
    
    status = fields.Selection([
        ('new', 'New'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('reopened', 'Reopened'),
        ('closed', 'Closed'),
    ], string="Status", default='new', tracking=True)
    
    assigned_to = fields.Many2one('res.users', string="Assigned To", tracking=True)
    reported_by = fields.Many2one('res.users', string="Reported By", default=lambda self: self.env.user)
    date_reported = fields.Datetime(string="Reported Date", default=fields.Datetime.now)
    date_closed = fields.Datetime(string="Closed Date")
    project_id = fields.Many2one('project.project', string="Project")
    tag_ids = fields.Many2many('bug.management.tag', string="Tags")
    attachment_ids = fields.Many2many('ir.attachment', string="Attachments")
    color = fields.Integer(string="Color Index")
    kanban_state = fields.Selection([
        ('normal', 'In Progress'),
        ('blocked', 'Blocked'),
        ('done', 'Ready for next stage')
    ], string='Kanban State', default='normal')
    
    # Computed fields
    days_open = fields.Integer(string="Days Open", compute='_compute_days_open', store=True)
    is_assigned = fields.Boolean(string="Is Assigned", compute='_compute_is_assigned', store=True)
    
    @api.depends('date_reported', 'date_closed')
    def _compute_days_open(self):
        for bug in self:
            if bug.date_closed:
                delta = bug.date_closed - bug.create_date
            else:
                delta = fields.Datetime.now() - bug.create_date
            bug.days_open = delta.days
    
    @api.depends('assigned_to')
    def _compute_is_assigned(self):
        for bug in self:
            bug.is_assigned = bool(bug.assigned_to)
    
    def action_assign_to_me(self):
        self.ensure_one()
        self.write({'assigned_to': self.env.user.id})
    
    def action_start_progress(self):
        self.ensure_one()
        if not self.assigned_to:
            raise UserError(_("Please assign the bug first."))
        self.write({'status': 'in_progress'})
    
    def action_resolve(self):
        self.ensure_one()
        self.write({
            'status': 'resolved',
            'date_closed': fields.Datetime.now()
        })
    
    def action_reopen(self):
        self.ensure_one()
        self.write({'status': 'reopened'})
    
    def action_close(self):
        self.ensure_one()
        self.write({
            'status': 'closed',
            'date_closed': fields.Datetime.now()
        })
    
    @api.constrains('severity', 'priority')
    def _check_priority_severity(self):
        for bug in self:
            if bug.severity == 'critical' and bug.priority in ['0', '1']:
                raise ValidationError(_("A critical severity bug must have high or critical priority."))
    
    def name_get(self):
        result = []
        for bug in self:
            name = "[%s] %s" % (bug.severity.upper(), bug.name)
            result.append((bug.id, name))
        return result