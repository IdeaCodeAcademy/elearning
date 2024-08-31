from odoo import api, fields, models


class IcaCourseModule(models.Model):
    _name = 'ica.course.module'
    _description = 'IcaCourseModule'

    name = fields.Char()
    course_id = fields.Many2one('ica.course', string='Course')
    lesson_ids = fields.One2many('ica.course.lesson', 'module_id', string='Lessons')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('unpublished', 'Unpublished'),
    ], default='draft')
