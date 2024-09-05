from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    latitude = fields.Char()
    longitude = fields.Char()

