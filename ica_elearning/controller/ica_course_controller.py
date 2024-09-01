from odoo.http import Controller, route, request


class IcaCourseController(Controller):
    @route('/ica/home', auth="public", type="http",website=True)
    def index(self):
        return request.render('ica_elearning.home', {})