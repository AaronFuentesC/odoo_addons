from odoo import models, fields


class hr_employee(models.Model):
    _inherit = 'hr.employee' # Heredamos el modelo hr.employee
    # Campo One2many para relacionar las multas con el empleado
    vehiculos_ids = fields.One2many('gestor_vehiculos_aaron.vehiculo', 'empleado_id', string='Vehículos')