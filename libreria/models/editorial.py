from odoo import models, fields
class editorial(models.Model):
    _name = 'libreria.editorial'
    _description = 'Editorial de libros'
    name = fields.Char(string="Nombre de la Editorial", required=True)
    libros_ids = fields.One2many('libreria.libro', 'editorial_id',string="Libros publicados")