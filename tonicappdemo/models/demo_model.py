from odoo import models, fields


class TonicDemo(models.Model):
    _name = "tonic.demo"
    _description = "Tonic Demo Model"

    name = fields.Char(required=True)
    description = fields.Text()
