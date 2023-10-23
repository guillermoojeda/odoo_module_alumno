from odoo import fields, models


class Inscripcion(models.Model):
    _name = 'escuela.inscripcion'
    _description = 'Incripciones de alumnos a cursos'

    alumno_id = fields.Many2one(
        'escuela.alumno',
        string='Alumno inscripto',
        required=True
    )
    programa_id = fields.Many2one(
        'escuela.programa',
        string='Nombre del programa',
        required=True
    )
    numero_de_tramite = fields.Integer()
