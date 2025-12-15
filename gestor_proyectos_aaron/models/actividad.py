from odoo import models, fields, api


class actividad(models.Model):
    _name = 'gestor_proyectos_aaron.actividad'
    _description = 'gestor_proyectos_aaron.actividad'

    descripcionTrabajo = fields.Char(string = "Descripción del actividad")
    fechaInicio = fields.Date(string = "Fecha de inicio")
    fechaFin = fields.Date(string = "Fecha de fin")
    #estadoTrabajo = fields.Text() 
    responsableActividad = fields.Text(string = "Responsable de la actividad")
    #importanciaActividades = fields.Text()
    #promedioDeAvance = fields.Integer(string = "Porcentaje individual")
    state = fields.Selection(
        [
            ('pending', 'Pendiente'),
            ('progress', 'En curso'),
            ('review', 'En revisión'),
            ('done', 'Finalizada'),
            ('cancel', 'Cancelada'),
        ],
        string="Estado",
        default='pending'
    )




    trabajo_id = fields.Many2one(
        'gestor_proyectos_aaron.trabajo',
        string="Id trabajo",
        required=True,
        ondelete='cascade'
    )