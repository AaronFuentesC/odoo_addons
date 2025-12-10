# from odoo import http


# class GestorProyectosAaron(http.Controller):
#     @http.route('/gestor_proyectos_aaron/gestor_proyectos_aaron', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestor_proyectos_aaron/gestor_proyectos_aaron/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestor_proyectos_aaron.listing', {
#             'root': '/gestor_proyectos_aaron/gestor_proyectos_aaron',
#             'objects': http.request.env['gestor_proyectos_aaron.gestor_proyectos_aaron'].search([]),
#         })

#     @http.route('/gestor_proyectos_aaron/gestor_proyectos_aaron/objects/<model("gestor_proyectos_aaron.gestor_proyectos_aaron"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestor_proyectos_aaron.object', {
#             'object': obj
#         })

