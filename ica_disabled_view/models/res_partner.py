from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    username = fields.Char()
    late_boolean = fields.Boolean(default=False)

    def action_sepica_effect(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'type': 'sepia',
            }
        }

