from odoo import api, fields, models


class IcaCourseModule(models.Model):
    _name = 'ica.course.module'
    _description = 'IcaCourseModule'

    name = fields.Char()
    course_id = fields.Many2one('ica.course', string='Course')
