from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    course_ids = fields.One2many('ica.course.enrollment.line', 'partner_id')
