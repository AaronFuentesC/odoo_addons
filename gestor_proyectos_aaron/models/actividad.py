from odoo import models, fields, api


class actividad(models.Model):
    _name = 'gestor_proyectos_aaron.actividad'
    _description = 'gestor_proyectos_aaron.actividad'

    descripcionActividad = fields.Char(string = "Descripción del actividad")
    fechaInicio = fields.Date(string = "Fecha de inicio")
    fechaFin = fields.Date(string = "Fecha de fin")
    porcentajeIndividual = fields.Integer(string = "Porcentaje individual")
    responsableActividad = fields.Many2one('res.users',string='Resposable de la actividad')
    state_id = fields.Many2one(
    'gestor_proyectos_aaron.estado',
    string="Estado"
    )





    trabajo_id = fields.Many2one(
        'gestor_proyectos_aaron.trabajo',
        string="Id trabajo",
        required=True,
        ondelete='cascade'
    )