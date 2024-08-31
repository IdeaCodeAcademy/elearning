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
    enrollment_ids = fields.One2many('ica.course.enrollment', 'course_id', string='Enrollment', )
    enrollment_count = fields.Integer(compute="_compute_enrollment_count")

    @api.depends('enrollment_ids')
    def _compute_enrollment_count(self):
        for rec in self:
            rec.enrollment_count = len(rec.enrollment_ids)

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

    enrollment_ids = fields.One2many('ica.course.enrollment', 'course_id', string='Enrollment', )
    enrollment_count = fields.Integer(compute="_compute_enrollment_count")

    @api.depends('enrollment_ids')
    def _compute_enrollment_count(self):
        for rec in self:
            rec.enrollment_count = len(rec.enrollment_ids)

    def action_view_enrollment(self):
        return {
            "name": f"{self.name}'s Enrollment",
            "type": "ir.actions.act_window",
            "res_model": "ica.course.enrollment",
            "view_mode": "tree,form",
            "domain": [("course_id", "=", self.id)],
            "context": {"default_course_id": self.id},
        }

    def action_self_enrollment(self):
        current_partner = self.env.user.partner_id.id
        if current_partner in self.enrollment_ids.partner_id.ids:
            raise UserError(_("You are already enrolled in this course."))
        # self.enrollment_ids.create({'partner_id': self.env.user.partner_id.id, 'course_id': self.id})
        # data = {
        #     "enrollment_ids": [fields.Command.create({"partner_id": current_partner})]
        # }
        data = {"enrollment_ids": [(0, 0, {"partner_id": current_partner})]}
        self.write(data)

    feedback_ids = fields.One2many('ica.course.feedback', 'course_id')
