from odoo import fields, models


class Programa(models.Model):
    _name = 'escuela.programa'
    _description = 'Programas del curso'

    nombre = fields.Char('Nombre')
    descripcion = fields.Text('Descripción')

    '''
    Hacer funcion que retorne cada uno de los anotados a un programa.
    [
		{
			'nombre': 'Cristian',
			'apellido': 'Ruppert',
			'legajo': 12548,
			'fecha_nacimiento': '1993-10-29'
			'email': 'cristian.ruppert@aden.org',
			'telefono': '+5492616861427',
			'pais': {
				'id': 587,
				'nombre': 'Argentina'
			}
		},
		{
			'nombre': 'Philipp',
			'apellido': 'Anderson',
			'legajo': 12549,
			'fecha_nacimiento': '1989-04-30'
			'email': 'philipp.anderson@test.com',
			'telefono': '+54912311111',
			'pais': {
				'id': 587,
				'nombre': 'Argentina'
			}
		}
	]'''

    # Intento Fallido aquí:
    #
    # alumnos = fields.Text(
    #     'Alumnos inscriptos',
    #     compute='_compute_students_in_program'
    # )

    # def get_registered_students(self, programa):
    #     students = self._cr.execute(
    #         'SELECT nombre, apellido FROM product_product ' +
    #         'JOIN escuela_inscripcion.alumno_id ON escuela_alumno.id = escuela_inscripcion.id ' +
    #         'JOIN escuela_programa ON  escuela_inscripcion.programa_id = escuela_programa.id ' +
    #         f'WHERE escuela_programa = {programa}'
    #     )
    #     return students

    # def _compute_students_in_program(self):
    #     for programa in self:
    #         students = self.get_registered_students(self.nombre)
    #         print(students)
    #         programa.alumnos_inscriptos = students
