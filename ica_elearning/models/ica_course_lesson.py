from odoo import api, fields, models


class IcaCourseLesson(models.Model):
    _name = 'ica.course.lesson'
    _description = 'IcaCourseLesson'

    name = fields.Char(required=True)
    course_id = fields.Many2one('ica.course', string='Course', required=True,
                                domain=[('state', '=', 'published')])
    module_id = fields.Many2one('ica.course.module', string='Module',
                                domain=[('course_id', '=', course_id),
                                        ('state', '=', 'published')])
    state = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('unpublished', 'Unpublished'),
    ], default='draft')
    preview = fields.Image(string='Preview')
    video = fields.Binary(string='Video')
