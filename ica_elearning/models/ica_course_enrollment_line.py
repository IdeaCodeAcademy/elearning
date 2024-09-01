from odoo import api, fields, models


class IcaCourseEnrollmentLine(models.Model):
    _name = 'ica.course.enrollment.line'
    _description = 'Ica Course Enrollment Line'

    enrollment_id = fields.Many2one('ica.course.enrollment')
    partner_id = fields.Many2one('res.partner',related='enrollment_id.partner_id')
    course_id = fields.Many2one('ica.course', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency', related="enrollment_id.currency_id")
    fees = fields.Monetary(currency_field="currency_id")

    @api.onchange('course_id')
    def _onchange_course_id(self):
        if self.course_id:
            self.fees = self.course_id.fees
