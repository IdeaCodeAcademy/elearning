from odoo import api, fields, models


class IcaCourseModule(models.Model):
    _name = 'ica.course.module'
    _description = 'IcaCourseModule'

    name = fields.Char()

    def _get_author_domain(self):
        return [('author_ids', 'in', self.env.user.partner_id.id)]

    course_id = fields.Many2one('ica.course', string='Course', domain=lambda self:[('author_ids', 'in', self.env.user.partner_id.id)])
    lesson_ids = fields.One2many('ica.course.lesson', 'module_id', string='Lessons')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('unpublished', 'Unpublished'),
    ], default='draft')
