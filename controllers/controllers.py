# -*- coding: utf-8 -*-
from odoo import http

# class LinkBank(http.Controller):
#     @http.route('/link_bank/link_bank/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/link_bank/link_bank/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('link_bank.listing', {
#             'root': '/link_bank/link_bank',
#             'objects': http.request.env['link_bank.link_bank'].search([]),
#         })

#     @http.route('/link_bank/link_bank/objects/<model("link_bank.link_bank"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('link_bank.object', {
#             'object': obj
#         })