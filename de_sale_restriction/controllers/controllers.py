# -*- coding: utf-8 -*-
# from odoo import http


# class DeSaleRestriction(http.Controller):
#     @http.route('/de_sale_restriction/de_sale_restriction/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_sale_restriction/de_sale_restriction/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_sale_restriction.listing', {
#             'root': '/de_sale_restriction/de_sale_restriction',
#             'objects': http.request.env['de_sale_restriction.de_sale_restriction'].search([]),
#         })

#     @http.route('/de_sale_restriction/de_sale_restriction/objects/<model("de_sale_restriction.de_sale_restriction"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_sale_restriction.object', {
#             'object': obj
#         })
