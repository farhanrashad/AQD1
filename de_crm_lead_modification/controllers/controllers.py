# -*- coding: utf-8 -*-
# from odoo import http


# class DeCrmFormModification(http.Controller):
#     @http.route('/de_crm_form_modification/de_crm_form_modification/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_crm_form_modification/de_crm_form_modification/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_crm_form_modification.listing', {
#             'root': '/de_crm_form_modification/de_crm_form_modification',
#             'objects': http.request.env['de_crm_form_modification.de_crm_form_modification'].search([]),
#         })

#     @http.route('/de_crm_form_modification/de_crm_form_modification/objects/<model("de_crm_form_modification.de_crm_form_modification"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_crm_form_modification.object', {
#             'object': obj
#         })
