from odoo import models, fields

class EstadoProyecto(models.Model):
    _name = 'gestor_proyectos_aaron.estado'
    _description = 'Estados de proyecto, trabajo y actividad'

    name = fields.Char(string="Nombre del estado", required=True)
    code = fields.Char(string="Código", required=True)

