from odoo import models, fields, api
from odoo.exceptions import ValidationError


class actividad(models.Model):
    _name = 'gestor_proyectos_aaron.actividad'
    _description = 'gestor_proyectos_aaron.actividad'

    descripcionActividad = fields.Char(string="Descripción de la actividad")
    fechaInicio = fields.Date(string="Fecha de inicio")
    fechaFin = fields.Date(string="Fecha de fin")
    porcentajeIndividual = fields.Integer(string="Porcentaje individual")
    responsableActividad = fields.Many2one(
        'res.users', string='Responsable de la actividad'
    )

    trabajo_id = fields.Many2one(
        'gestor_proyectos_aaron.trabajo',
        string="Trabajo",
        required=True,
        ondelete='cascade'
    )

    state_id = fields.Many2one(
        'gestor_proyectos_aaron.estado',
        string="Estado",
        compute="_compute_estado_por_porcentaje",
        store=True
    )

    # -------------------------
    # VALIDACIÓN PORCENTAJE
    # -------------------------
    @api.constrains('porcentajeIndividual')
    def _check_porcentaje(self):
        for actividad in self:
            if not 0 <= actividad.porcentajeIndividual <= 100:
                raise ValidationError(
                    "El porcentaje de avance debe estar entre 0 y 100."
                )

    # -------------------------
    # VALIDACIÓN FECHAS
    # -------------------------
    @api.constrains('fechaInicio', 'fechaFin', 'trabajo_id')
    def _check_fechas_actividad_en_trabajo(self):
        for actividad in self:
            trabajo = actividad.trabajo_id
            if not trabajo:
                continue

            if actividad.fechaInicio and trabajo.fechaInicio:
                if actividad.fechaInicio < trabajo.fechaInicio:
                    raise ValidationError(
                        "La fecha de inicio de la actividad no puede ser anterior a la del trabajo."
                    )

            if actividad.fechaFin and trabajo.fechaFin:
                if actividad.fechaFin > trabajo.fechaFin:
                    raise ValidationError(
                        "La fecha de fin de la actividad no puede ser posterior a la del trabajo."
                    )

            if actividad.fechaInicio and actividad.fechaFin:
                if actividad.fechaInicio > actividad.fechaFin:
                    raise ValidationError(
                        "La fecha de inicio no puede ser posterior a la fecha de fin."
                    )

    # -------------------------
    # ESTADO AUTOMÁTICO
    # -------------------------
    @api.depends('porcentajeIndividual')
    def _compute_estado_por_porcentaje(self):
        estado_done = self.env['gestor_proyectos_aaron.estado'].search(
            [('code', '=', 'done')], limit=1
        )
        estado_progress = self.env['gestor_proyectos_aaron.estado'].search(
            [('code', '=', 'progress')], limit=1
        )
        estado_pending = self.env['gestor_proyectos_aaron.estado'].search(
            [('code', '=', 'pending')], limit=1
        )

        for actividad in self:
            if actividad.porcentajeIndividual == 100 and estado_done:
                actividad.state_id = estado_done
            elif actividad.porcentajeIndividual > 0 and estado_progress:
                actividad.state_id = estado_progress
            elif estado_pending:
                actividad.state_id = estado_pending
