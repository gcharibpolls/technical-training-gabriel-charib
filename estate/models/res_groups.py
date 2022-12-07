from odoo import fields, models

#base des donnes

class ResGroups(models.Model):
    _inherit = 'res.groups'

    max_amount = fields.Float(String = "training Max price")
