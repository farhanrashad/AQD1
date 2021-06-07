# -*- coding: utf-8 -*-
# from odoo import http


# class DeSaleProductExt(http.Controller):
#     @http.route('/de_sale_product_ext/de_sale_product_ext/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_sale_product_ext/de_sale_product_ext/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_sale_product_ext.listing', {
#             'root': '/de_sale_product_ext/de_sale_product_ext',
#             'objects': http.request.env['de_sale_product_ext.de_sale_product_ext'].search([]),
#         })

#     @http.route('/de_sale_product_ext/de_sale_product_ext/objects/<model("de_sale_product_ext.de_sale_product_ext"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_sale_product_ext.object', {
#             'object': obj
#         })
