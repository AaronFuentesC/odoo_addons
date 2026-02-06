from odoo import models, fields

class VehiculoHistorico(models.Model):
    _name = 'gestor_vehiculos_aaron.vehiculo_historico'
    _description = 'Histórico de asignaciones de vehículos'

    vehiculo_id = fields.Many2one(
        'gestor_vehiculos_aaron.vehiculo',
        string="Vehículo",
        required=True,
        ondelete='cascade'
    )

    empleado_id = fields.Many2one(
        'hr.employee',
        string="Empleado"
    )

    fecha_inicio = fields.Datetime(
        string="Fecha inicio",
        default=fields.Datetime.now
    )

    fecha_fin = fields.Datetime(
        string="Fecha fin"
    )
    activo = fields.Boolean(default=True)
    
