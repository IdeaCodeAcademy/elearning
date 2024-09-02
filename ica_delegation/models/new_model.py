from odoo import api, fields, models

class NewSampleModel(models.Model):
    _name = 'new.model'
    _description = 'New Model'
    _inherits = {'sample.model': 'sample_model_id'}

    name = fields.Char()
    sample_model_id = fields.Many2one('sample.model')
