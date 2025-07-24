class ManagementBug(models.Model):
    _name = 'management.bug'
    _description = 'Management Bug'

    name = fields.Char(string='Bug Title', required=True)
    description = fields.Text(string='Description')
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ], string='Status', default='new')
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], string='Priority', default='medium')
    assigned_to = fields.Many2one('res.users', string='Assigned To')
    created_date = fields.Datetime(string='Created Date', default=fields.Datetime.now)
    updated_date = fields.Datetime(string='Updated Date', default=fields.Datetime.now)