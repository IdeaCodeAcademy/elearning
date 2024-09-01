from odoo.http import Controller, route, request


class IcaCourseController(Controller):
    @route(['/ica/home', '/ica/course/details/<model("ica.course"):course_id>'], auth="user", type="http", website=True)
    def index(self, course_id=None, **kwargs):
        if course_id:
            return request.render('ica_elearning.course_details', {'course_id': course_id})
        course_ids = request.env['ica.course'].search([('state', '=', 'published')])
        return request.render('ica_elearning.home', {'course_ids': course_ids})

    @route(['/api/ica/courses', '/api/ica/course/details/<model("ica.course"):course_id>'], type="json", auth="user")
    def api_courses(self, course_id=None, **kwargs):
        if course_id:
            return {"course_id": course_id.sudo()}
        course_ids = request.env['ica.course'].sudo().search_read(domain=[('state', '=', 'published')],
                                                                  fields=['id', 'name', 'fees', 'state'])
        data = list(map(lambda x: {**x, 'detail': f'/api/ica/course/details/{x["id"]}'}, course_ids))
        return {"course_ids": data}

    @route('/api/login', type="json", auth="none")
    def api_login(self, username, password, **kw):
        uid = request.session.authenticate(request.session.db, username, password)
        return {"message": "Login Successful", "uid": uid}
