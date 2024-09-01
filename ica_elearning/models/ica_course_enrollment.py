from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class IcaCourseEnrollment(models.Model):
    _name = 'ica.course.enrollment'
    _description = 'Ica Course Enrollment'
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    total_amount = fields.Monetary(currency_field='currency_id', compute="_compute_total_amount")
    line_ids = fields.One2many('ica.course.enrollment.line', 'enrollment_id')
    name = fields.Char(default=lambda self: _("New"))

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Enrollment name must be unique'),
    ]

    # @api.constrains('name')
    # def _check_description(self):
    #     for record in self:
    #         domain = [('id', '!=', record.id)]
    #         enrollment_ids = self.search(domain)
    #         if record.name in enrollment_ids.mapped('name'):
    #             raise ValidationError(_("Enrollment name must be unique"))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code(self._name)
        return super(IcaCourseEnrollment, self).create(vals_list)

    @api.depends('line_ids')
    def _compute_total_amount(self):
        for rec in self:
            rec.total_amount = sum(rec.line_ids.mapped('fees'))
