from odoo import api, fields, models


class IcaCourseFeedbackWizard(models.TransientModel):
    _name = 'ica.course.feedback.wizard'
    _description = 'IcaCourseFeedbackWizard'

    review = fields.Text(string='Review')

    def action_add_review(self):
        context = self.env.context
        active_id = context.get('active_id')
        data = {
            "course_id": active_id,
            "partner_id": self.env.user.partner_id.id,
            "review": self.review,
        }
        self.env['ica.course.feedback'].create(data)
