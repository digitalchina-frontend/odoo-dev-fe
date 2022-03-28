# -*- coding: utf-8 -*-
# from odoo import http


# class ThemeAwesome(http.Controller):
#     @http.route('/theme_awesome/theme_awesome/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/theme_awesome/theme_awesome/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('theme_awesome.listing', {
#             'root': '/theme_awesome/theme_awesome',
#             'objects': http.request.env['theme_awesome.theme_awesome'].search([]),
#         })

#     @http.route('/theme_awesome/theme_awesome/objects/<model("theme_awesome.theme_awesome"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('theme_awesome.object', {
#             'object': obj
#         })
