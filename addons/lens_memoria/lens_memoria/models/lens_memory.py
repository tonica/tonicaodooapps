from odoo import models, fields


class LensMemory(models.Model):
    _name = 'lens.memory'
    _description = 'Lens Memory'

    name = fields.Char(string='Name', required=True)
    date_taken = fields.Date(string='Date Taken')
    photo = fields.Binary(string='Photo')
    image_filename = fields.Char(string='Photo Filename')
    photographer_id = fields.Many2one('res.partner', string='Photographer')
    location = fields.Char(string='Location')
    camera = fields.Char(string='Camera')
    category_id = fields.Many2one('lens.category', string='Category')
    tag_ids = fields.Many2many('lens.tag', string='Tags')
    notes = fields.Text(string='Notes')
    state = fields.Selection([
        ('new', 'New'),
        ('archived', 'Archived'),
    ], string='State', default='new')
    is_public = fields.Boolean(string='Public', default=False)


class LensCategory(models.Model):
    _name = 'lens.category'
    _description = 'Lens Category'

    name = fields.Char(string='Name', required=True)


class LensTag(models.Model):
    _name = 'lens.tag'
    _description = 'Lens Tag'

    name = fields.Char(string='Name', required=True)
