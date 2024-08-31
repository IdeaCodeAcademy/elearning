from odoo import api, fields, models


class IcaCourseFeedback(models.Model):
    _name = 'ica.course.feedback'
    _description = 'IcaCourseFeedback'
    _rec_name = 'partner_id'

    course_id = fields.Many2one('ica.course', string='Course')
    partner_id = fields.Many2one('res.partner', string='Partner', default=lambda self: self.env.user.partner_id)
    review = fields.Text(string='Review')
