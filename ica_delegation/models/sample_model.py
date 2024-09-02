from odoo import api, fields, models


class SampleModel(models.Model):
    _name = 'sample.model'
    _description = 'SampleModel'

    name = fields.Char()
    age = fields.Integer()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='male')