from odoo import models, fields, api
from odoo.exceptions import UserError


class Vehiculo(models.Model):
    _name = 'gestor_vehiculos_aaron.vehiculo'
    _description = 'Vehículos de los empleados'

    # Campo para la fecha en que se impone la multa
    kilometros = fields.Integer(string="Kilometros", required=True)
    # Campo de texto para describir la razón de la multa
    matricula = fields.Char(string="Matrícula", required=True)

    marca = fields.Text(string="Marca",required=True)

    modelo = fields.Text(string="Modelo", required=True)

    # Relación Many2one con el modelo 'hr.employee' (empleado que tiene el vehículo)
    empleado_id = fields.Many2one(
        'hr.employee',
        string="Empleado",
        required=False
    )
    # Campo calculado basado en el nombre del empleado
    nombre_empleado = fields.Char(string="Nombre Empleado", related='empleado_id.name')

    disponible = fields.Boolean(
    string="Disponible",
    compute="_compute_disponible",
    store=True
    )

    historico_ids = fields.One2many(
    'gestor_vehiculos_aaron.vehiculo_historico',
    'vehiculo_id',
    string="Histórico"
)


    @api.depends('empleado_id')
    def _compute_disponible(self):
        for v in self:
            v.disponible = not bool(v.empleado_id)


    activo = fields.Boolean(default=True)

    def unlink(self):
        raise UserError("No se pueden borrar vehículos, solo darlos de baja.")

    _sql_constraints = [
        ('matricula_unique', 'unique(matricula)', 'La matrícula ya existe.')
]


    def write(self, vals):
        res = super().write(vals)

        if 'empleado_id' in vals:
            for vehiculo in self:

                #Cerrar histórico activo anterior
                historico_activo = self.env[
                    'gestor_vehiculos_aaron.vehiculo_historico'
                ].search([
                    ('vehiculo_id', '=', vehiculo.id),
                    ('activo', '=', True)
                ], limit=1)

                if historico_activo:
                    historico_activo.write({
                        'fecha_fin': fields.Datetime.now(),
                        'activo': False,
                    })

                #Crear nuevo histórico si hay empleado
                if vehiculo.empleado_id:
                    self.env[
                        'gestor_vehiculos_aaron.vehiculo_historico'
                    ].create({
                        'vehiculo_id': vehiculo.id,
                        'empleado_id': vehiculo.empleado_id.id,
                        'fecha_inicio': fields.Datetime.now(),
                        'activo': True,
                    })

        return res







