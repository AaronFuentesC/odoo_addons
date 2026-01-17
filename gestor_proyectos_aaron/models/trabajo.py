from odoo import models, fields, api
from odoo.exceptions import ValidationError


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

        




    @api.depends('actividades_ids.porcentajeIndividual')
    def _compute_porcentaje_avance(self):
        Estado = self.env['gestor_proyectos_aaron.estado']
        estado_done = Estado.search([('code', '=', 'done')], limit=1)
        estado_progress = Estado.search([('code', '=', 'progress')], limit=1)
        estado_pending = Estado.search([('code', '=', 'pending')], limit=1)

        for trabajo in self:
            actividades = trabajo.actividades_ids

            if not actividades:
                trabajo.porcentaje_avance = 0.0
                trabajo.state_id = estado_pending
                continue

            total = sum(a.porcentajeIndividual for a in actividades)
            trabajo.porcentaje_avance = total / len(actividades)

            # SINCRONIZACIÓN DE ESTADO
            if trabajo.porcentaje_avance == 100.0:
                trabajo.state_id = estado_done
            elif trabajo.porcentaje_avance > 0:
                trabajo.state_id = estado_progress
            else:
                trabajo.state_id = estado_pending







    @api.constrains('fechaInicio', 'fechaFin', 'proyecto_id')
    def _check_fechas_trabajo_en_proyecto(self):
        for trabajo in self:
            proyecto = trabajo.proyecto_id
            if not proyecto:
                continue

            if trabajo.fechaInicio and proyecto.fechaInicio:
                if trabajo.fechaInicio < proyecto.fechaInicio:
                    raise ValidationError(
                        "La fecha de inicio del trabajo no puede ser anterior a la del proyecto."
                    )

            if trabajo.fechaFin and proyecto.fechaFin:
                if trabajo.fechaFin > proyecto.fechaFin:
                    raise ValidationError(
                        "La fecha de fin del trabajo no puede ser posterior a la del proyecto."
                    )

            if trabajo.fechaInicio and trabajo.fechaFin:
                if trabajo.fechaInicio > trabajo.fechaFin:
                    raise ValidationError(
                        "La fecha de inicio del trabajo no puede ser posterior a la fecha de fin."
                    )



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