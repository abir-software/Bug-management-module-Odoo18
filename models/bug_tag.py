from odoo import models, fields, api

class BugTag(models.Model):
    _name = 'bug.management.tag'
    _description = 'Bug Tag'
    _order = 'name'

    name = fields.Char(string='Tag Name', required=True, translate=True)
    color = fields.Integer(string='Color Index')
    
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists!"),
    ]