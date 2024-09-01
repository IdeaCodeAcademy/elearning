from odoo.http import Controller, route


class MainController(Controller):
    @route('/some_url', auth='public')
    def handler(self):
        return stuff()


class Extension(MainController):
    @route()
    def handler(self):
        do_before()
        return super(Extension, self).handler()


class Restrict(MainController):

    @route(auth='user')
    def handler(self):
        return super(Restrict, self).handler()
