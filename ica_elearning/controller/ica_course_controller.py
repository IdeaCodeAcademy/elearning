from odoo.http import Controller, route, request


class IcaCourseController(Controller):
    @route('/ica/home', auth="public", type="http", website=True)
    def index(self):
        course_ids = request.env['ica.course'].search([('state', '=', 'published')])
        return request.render('ica_elearning.home', {'course_ids': course_ids})
