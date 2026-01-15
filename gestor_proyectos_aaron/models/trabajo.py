from odoo import models, fields, api

class trabajo(models.Model):
    _name = 'gestor_proyectos_aaron.trabajo'
    _description = 'gestor_proyectos_aaron.trabajo'

    descripcionTrabajo = fields.Char(string = "Descripción del trabajo")
    fechaInicio = fields.Date(string = "Fecha de inicio")
    fechaFin = fields.Date(string = "Fecha de fin")
    responsableTrabajo = fields.Many2one('res.users',string='Resposable del trabajo')
    #importanciaActividades = fields.Text()
    #promedioDeAvance = fields.Integer(string = "Porcentaje individual")

    
    porcentaje_avance = fields.Float(
    string="Progreso del trabajo (%)",
    compute="_compute_porcentaje_avance",
    store=True
    )

        




    @api.depends('actividades_ids.state_id')
    def _compute_porcentaje_avance(self):
        for trabajo in self:
            total = len(trabajo.actividades_ids)

            if total == 0:
                trabajo.porcentaje_avance = 0.0
            else:
                actividades_finalizadas = trabajo.actividades_ids.filtered(
                    lambda a: a.state_id.code == 'done'
                )
                trabajo.porcentaje_avance = (len(actividades_finalizadas) / total) * 100

            if trabajo.porcentaje_avance == 100.0:
                estado_final = self.env['gestor_proyectos_aaron.estado'].search(
                    [('code', '=', 'done')], limit=1
                )
                if estado_final:
                    trabajo.state_id = estado_final



    state_id = fields.Many2one(
        'gestor_proyectos_aaron.estado',
        string="Estado"
    )





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