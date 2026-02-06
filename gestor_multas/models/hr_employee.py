from odoo import models, fields


class hr_employee(models.Model):
    _inherit = 'hr.employee' # Heredamos el modelo hr.employee
    # Campo One2many para relacionar las multas con el empleado
    multa_ids = fields.One2many('gestion.multa', 'empleado_id', string='Multas')