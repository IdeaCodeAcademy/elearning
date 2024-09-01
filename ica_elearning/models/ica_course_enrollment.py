from odoo import api, fields, models


class IcaCourseEnrollment(models.Model):
    _name = 'ica.course.enrollment'
    _description = 'Ica Course Enrollment'
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    total_amount = fields.Monetary(currency_field='currency_id',compute="_compute_total_amount")
    line_ids = fields.One2many('ica.course.enrollment.line', 'enrollment_id')

    @api.depends('line_ids')
    def _compute_total_amount(self):
        self.total_amount = sum(self.line_ids.mapped('fees'))
