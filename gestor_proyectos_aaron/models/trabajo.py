from odoo import models, fields, api

class trabajo(models.Model):
    _name = 'gestor_proyectos_aaron.trabajo'
    _description = 'gestor_proyectos_aaron.trabajo'

    descripcionTrabajo = fields.Char(string = "Descripción del trabajo")
    fechaInicio = fields.Date(string = "Fecha de inicio")
    fechaFin = fields.Date(string = "Fecha de fin")
    #estadoTrabajo = fields.Text() 
    responsableTrabajo = fields.Text(string = "Responsable del trabajo")
    #importanciaActividades = fields.Text()
    #promedioDeAvance = fields.Integer(string = "Porcentaje individual")
    proyecto_id = fields.Many2one(
        'gestor_proyectos_aaron.proyecto',
        string="Id proyecto",
        required=True,
        ondelete='cascade'
    )

    actividades_ids = fields.One2many(
        'gestor_proyectos_aaron.actividad',
        'trabajo_id',
        string="Actividades asociadas"
    )