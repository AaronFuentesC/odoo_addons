from odoo import models, fields, api



#Nombre del proyecto, Descripción general del proyecto, Fecha de inicio,
#Fecha de fin, estado del proyecto, responsable del proyecto, porcentaje
#de avance respecto a partir de trabajos y actividades, relación con
#trabajos del proyecto, Avance individual (0–100%)



class proyecto(models.Model):
    _name = 'gestor_proyectos_aaron.proyecto'
    _description = 'gestor_proyectos_aaron.proyecto'

    nombreProyecto = fields.Char(string="Nombre del proyecto")
    descripcionProyecto = fields.Char(string = "Descripción del proyecto")
    fechaInicio = fields.Date(string = "Fecha de inicio")
    fechaFin = fields.Date(string = "Fecha de fin")
    #estadoProyecto = fields.Text()
    responsableProyecto = fields.Text(string = "Responsable del proyecto")
    #porcentajeAvance = fields.Float()
    porcentajeIndividual = fields.Integer(string = "Porcentaje individual")

    trabajos_ids = fields.One2many(
        'gestor_proyectos_aaron.trabajo',
        'proyecto_id',
        string="Trabajos asociados"
    )

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

