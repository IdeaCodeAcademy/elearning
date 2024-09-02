from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    send_mail = fields.Boolean(config_parameter='ica_elearning.send_mail')