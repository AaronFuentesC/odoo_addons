from odoo import models, fields, api
from odoo.exceptions import UserError

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

    @api.depends('trabajos_ids.porcentaje_avance')
    def _compute_porcentaje_avance(self):
        Estado = self.env['gestor_proyectos_aaron.estado']
        estado_done = Estado.search([('code', '=', 'done')], limit=1)
        estado_progress = Estado.search([('code', '=', 'progress')], limit=1)
        estado_pending = Estado.search([('code', '=', 'pending')], limit=1)

        for proyecto in self:
            trabajos = proyecto.trabajos_ids

            if not trabajos:
                proyecto.porcentaje_avance = 0.0
                proyecto.state_id = estado_pending
                continue

            total = sum(t.porcentaje_avance for t in trabajos)
            proyecto.porcentaje_avance = total / len(trabajos)

            if proyecto.porcentaje_avance == 100.0:
                proyecto.state_id = estado_done
            elif proyecto.porcentaje_avance > 0:
                proyecto.state_id = estado_progress
            else:
                proyecto.state_id = estado_pending

    def unlink(self):
        for proyecto in self:
            if proyecto.trabajos_ids:
                raise UserError(
                    "No se puede eliminar un proyecto que tiene trabajos asociados."
                )
        return super().unlink()

    state_id = fields.Many2one(
    'gestor_proyectos_aaron.estado',
    string="Estado"
    )

    trabajos_ids = fields.One2many(
        'gestor_proyectos_aaron.trabajo',
        'proyecto_id',
        string="Trabajos asociados"
    )
