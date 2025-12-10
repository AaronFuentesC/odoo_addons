from odoo import models, fields, api

class autor(models.Model):
    _name = "libreria.autor"
    _description="Descripción del modulo autor"

    _rec_name = "nombre"

    nombre = fields.Char(string="Autor",required=True)

    libros_ids = fields.Many2many("libreria.libro",string="Libros")