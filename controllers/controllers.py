# -*- coding: utf-8 -*-
from odoo import http

# class ModuloProfesores(http.Controller):
#     @http.route('/modulo_profesores/modulo_profesores/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_profesores/modulo_profesores/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_profesores.listing', {
#             'root': '/modulo_profesores/modulo_profesores',
#             'objects': http.request.env['modulo_profesores.modulo_profesores'].search([]),
#         })

#     @http.route('/modulo_profesores/modulo_profesores/objects/<model("modulo_profesores.modulo_profesores"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_profesores.object', {
#             'object': obj
#         })