# from odoo import http


# class GestorMultas(http.Controller):
#     @http.route('/gestor_multas/gestor_multas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestor_multas/gestor_multas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestor_multas.listing', {
#             'root': '/gestor_multas/gestor_multas',
#             'objects': http.request.env['gestor_multas.gestor_multas'].search([]),
#         })

#     @http.route('/gestor_multas/gestor_multas/objects/<model("gestor_multas.gestor_multas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestor_multas.object', {
#             'object': obj
#         })

