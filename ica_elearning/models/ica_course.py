from odoo import api, fields, models


class IcaCourse(models.Model):
    _name = 'ica.course'
    _description = 'IcaCourse'

    name = fields.Char()
    description = fields.Text()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('unpublished', 'Unpublished'),
    ], default='draft')
    author_ids = fields.Many2many('res.partner', string='Authors')
    module_ids = fields.One2many('ica.course.module', 'course_id', string='Modules')
    lesson_ids = fields.One2many('ica.course.lesson', 'course_id', string='Lessons')
