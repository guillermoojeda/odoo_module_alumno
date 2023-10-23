from odoo import fields, models


class Alumno(models.Model):
    _name = "escuela.alumno"
    _description = "Alumnos del curso"
    # _order = "sequence"

    nombre = fields.Char('Nombre', required=True)
    apellido = fields.Char('Apellido', required=True)
    fecha_de_nacimiento = fields.Date('Fecha de Nacimiento')
    numero_de_legajo = fields.Integer('Número de legajo', required=True)
    email = fields.Char('Email')
    telefono = fields.Integer('Teléfono')
    direccion = fields.Char('Dirección')
    pais = fields.Char('País')
