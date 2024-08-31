from odoo import api, fields, models


class IcaCourseLesson(models.Model):
    _name = 'ica.course.lesson'
    _description = 'IcaCourseLesson'

    name = fields.Char()
    module_id = fields.Many2one('ica.course.module', string='Module')
    course_id = fields.Many2one('ica.course', related="module_id.course_id", string='Course')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('unpublished', 'Unpublished'),
    ], default='draft')
    preview = fields.Image(string='Preview')
    video = fields.Binary(string='Video')
