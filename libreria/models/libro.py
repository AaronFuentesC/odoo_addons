from odoo import models, fields, api


class libro(models.Model):
    _name = 'libreria.libro'
    _description = 'Descripción del módulo libro libreria.libro'
    autores_ids = fields.Many2many("libreria.autor",string="Autores")

    name = fields.Char(string="Titulo del Libro",required=True,help="Título del libro")
    description = fields.Text(string="Descripción del libro")
    numPaginas = fields.Integer()
    precio = fields.Float(string="Precio", digits=(10,2),help="Precio del libro en euros")
    is_available = fields.Boolean(string="¿Disponible?",default=True)
    publication_date = fields.Date(string="Fecha de publicación")
    created_datetime = fields.Datetime(string="Fecha y hora de registro",default=fields.Datetime.now)
    portada = fields.Image(string="Portada")
    # Relación Many2one: Libro -> Editorial
    editorial_id = fields.Many2one('libreria.editorial', string='Editorial',help="Editorial que publicó el libro")


    days_since_publication = fields.Integer(
        string="Días desde publicación",
        compute="_compute_days_since_publication",
        store=False

    )
    @api.depends('publication_date')
    def _compute_days_since_publication(self):
        for record in self:
            if record.publication_date:
                delta = date.today() - record.publication_date
                record.days_since_publication = delta.days
            else:
                record.days_since_publication = 0


#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

