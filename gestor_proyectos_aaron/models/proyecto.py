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
    responsableProyecto = fields.Many2one('res.users',string='Resposable del proyecto')

    porcentaje_avance = fields.Float(
    string="Progreso del proyecto (%)",
    compute="_compute_porcentaje_avance",
    store=True
    )

    @api.depends('trabajos_ids.state_id')
    def _compute_porcentaje_avance(self):
        for proyecto in self:
            total = len(proyecto.trabajos_ids)

            if total == 0:
                proyecto.porcentaje_avance = 0.0
            else:
                trabajos_finalizados = proyecto.trabajos_ids.filtered(
                    lambda t: t.state_id.code == 'done'
                )
                proyecto.porcentaje_avance = (len(trabajos_finalizados) / total) * 100

            if proyecto.porcentaje_avance == 100.0:
                estado_final = self.env['gestor_proyectos_aaron.estado'].search([('code', '=', 'done')], limit=1)
                if estado_final:
                    proyecto.state_id = estado_final


    state_id = fields.Many2one(
    'gestor_proyectos_aaron.estado',
    string="Estado"
    )

    trabajos_ids = fields.One2many(
        'gestor_proyectos_aaron.trabajo',
        'proyecto_id',
        string="Trabajos asociados"
    )
