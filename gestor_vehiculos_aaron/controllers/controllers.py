# from odoo import http


# class GestorVehiculosAaron(http.Controller):
#     @http.route('/gestor_vehiculos_aaron/gestor_vehiculos_aaron', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestor_vehiculos_aaron/gestor_vehiculos_aaron/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestor_vehiculos_aaron.listing', {
#             'root': '/gestor_vehiculos_aaron/gestor_vehiculos_aaron',
#             'objects': http.request.env['gestor_vehiculos_aaron.gestor_vehiculos_aaron'].search([]),
#         })

#     @http.route('/gestor_vehiculos_aaron/gestor_vehiculos_aaron/objects/<model("gestor_vehiculos_aaron.gestor_vehiculos_aaron"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestor_vehiculos_aaron.object', {
#             'object': obj
#         })

