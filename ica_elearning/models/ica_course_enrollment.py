from odoo import api, fields, models


class IcaCourseEnrollment(models.Model):
    _name = 'ica.course.enrollment'
    _description = 'Ica Course Enrollment'
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner')
    course_id = fields.Many2one('ica.course')
