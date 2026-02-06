from odoo import models, fields
class tipo_multa(models.Model):
    _name = 'gestion.tipo_multa'
    _description = 'Tipos de Multa'
    name = fields.Char(string="Tipo de sanción", required=True)