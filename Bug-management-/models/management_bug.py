# Bug management model placeholder
from odoo import models, fields

class ManagementBug(models.Model):
    _name = 'management.bug'
    _description = 'Management Bug'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    state = fields.Selection([
        ('new', 'New'),
        ('assigned', 'Assigned'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed')
    ], string='Status', default='new')
