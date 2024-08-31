from odoo import api, fields, models, _
from odoo.exceptions import UserError


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
    module_ids = fields.One2many('ica.course.module', 'course_id', string='Modules',
                                 domain=[('state', '=', 'published')])
    module_count = fields.Integer(string='Modules', compute="_compute_module_count")
    lesson_ids = fields.One2many('ica.course.lesson', 'course_id', string='Lessons',
                                 domain=[('state', '=', 'published')])
    lesson_count = fields.Integer(string='Lessons', compute="_compute_lesson_count")
    enrollment_ids = fields.One2many('ica.course.enrollment','course_id', string='Enrollment',)

    @api.depends('lesson_ids')
    def _compute_lesson_count(self):
        for rec in self:
            rec.lesson_count = len(rec.lesson_ids)

    @api.depends('module_ids')
    def _compute_module_count(self):
        for rec in self:
            rec.module_count = len(rec.module_ids)

    def action_draft(self):
        self.state = 'draft'

    def action_published(self):
        if not (self.module_ids and self.lesson_ids):
            raise UserError(_('you should have at least one lesson'))
        self.state = 'published'

    def action_unpublished(self):
        self.state = 'unpublished'

    def action_view_modules(self):
        return {
            "name": f"{self.name}'s Modules",
            "type": "ir.actions.act_window",
            "res_model": "ica.course.module",
            "view_mode": "tree,form",
            "domain": [("course_id", "=", self.id)],
            "context": {"default_course_id": self.id},
        }

    def action_view_lessons(self):
        return {
            "name": f"{self.name}'s Lessons",
            "type": "ir.actions.act_window",
            "res_model": "ica.course.lesson",
            "view_mode": "tree,form",
            "domain": [("course_id", "=", self.id)],
            "context": {"default_course_id": self.id},
        }
