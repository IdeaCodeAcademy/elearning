from odoo import api, fields, models


class IcaCourseLesson(models.Model):
    _name = 'ica.course.lesson'
    _description = 'IcaCourseLesson'

    name = fields.Char(required=True)

    def _get_author_domain(self):
        return [('author_ids', 'in', self.env.user.partner_id.id)]

    course_id = fields.Many2one('ica.course', string='Course', domain=_get_author_domain)
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
