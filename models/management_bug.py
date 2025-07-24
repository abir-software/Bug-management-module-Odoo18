from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class BugManagement(models.Model):
    _name = 'bug.management'
    _description = 'Bug Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    name = fields.Char(string='Bug Title', required=True, tracking=True)
    description = fields.Text('Description', required=True, tracking=True)
    steps_to_reproduce = fields.Text('Steps to Reproduce')
    severity = fields.Selection([
        ('minor', 'Minor'),
        ('major', 'Major'),
        ('critical', 'Critical'),
    ], string='Severity', default='minor', tracking=True)
    state = fields.Selection([
        ('new', 'New'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='new', tracking=True)
    reported_by_id = fields.Many2one('res.users', string='Reported By', default=lambda self: self.env.user, tracking=True)
    assigned_to_id = fields.Many2one('res.users', string='Assigned To', tracking=True)
    project_id = fields.Many2one('project.project', string='Project', tracking=True)
    solve_date = fields.Datetime('Solved Date', tracking=True)
    is_solved = fields.Boolean('Is Solved?', compute='_compute_is_solved', store=True)
    note = fields.Html('Internal Notes')

    # For Dashboard statistics
    solve_time = fields.Float('Time to Solve (hours)', compute='_compute_solve_time', store=True)
    closed_by_id = fields.Many2one('res.users', string='Closed By', tracking=True)
    tags = fields.Many2many('bug.management.tag', string="Tags")

    @api.depends('state', 'solve_date', 'create_date')
    def _compute_solve_time(self):
        for bug in self:
            if bug.solve_date and bug.create_date and bug.state in ['resolved', 'closed']:
                delta = fields.Datetime.from_string(bug.solve_date) - fields.Datetime.from_string(bug.create_date)
                bug.solve_time = delta.total_seconds() / 3600.0
            else:
                bug.solve_time = 0.0

    @api.depends('state')
    def _compute_is_solved(self):
        for bug in self:
            bug.is_solved = bug.state in ['resolved', 'closed']

    def action_assign(self):
        self.ensure_one()
        self.state = 'assigned'
        self.assigned_to_id = self.env.user.id

    def action_in_progress(self):
        self.ensure_one()
        self.state = 'in_progress'

    def action_resolve(self):
        self.ensure_one()
        self.state = 'resolved'
        self.solve_date = fields.Datetime.now()
        self.closed_by_id = self.env.user.id

    def action_close(self):
        self.ensure_one()
        self.state = 'closed'
        self.solve_date = fields.Datetime.now()
        self.closed_by_id = self.env.user.id

    def action_cancel(self):
        self.ensure_one()
        self.state = 'cancelled'

    @api.constrains('description')
    def _check_description(self):
        for bug in self:
            if len(bug.description) < 10:
                raise ValidationError(_("Bug description must be at least 10 characters long."))

class BugManagementTag(models.Model):
    _name = 'bug.management.tag'
    _description = 'Bug Tag'

    name = fields.Char(string="Tag", required=True, index=True)
    color = fields.Integer(string='Color')
