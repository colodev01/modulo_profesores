# -*- coding: utf-8 -*-

from odoo import models, fields, api

ESTADOS = [
    ('pendiente', 'Pendiente'),

]

class EscuelaInscripcion(models.Model):
    _name = 'escuela.inscripcion'
    # _rec_name = 'nombre_inscripcion'

    # nombre_inscripcion = fields.Char(string="Nombre Inscripcion", compute='set_nombre_inscripcion')
    nota = fields.Float(string="Nota final", default=0)
    fecha_inscripcion = fields.Date(string="Fecha de Inscripcion")
    estado_inscripcion = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('libre', 'Libre'),
        ('regular', 'Regular'),
        ('aprobado', 'Aprobado')
    ])

    alumno_id = fields.Many2one(
        comodel_name="escuela.alumno", string="Alumno"
    )
    materia_id = fields.Many2one(
        comodel_name="escuela.materia", string="Materia"
    )

    @api.onchange('nota')
    def set_estado_inscripcion(self):
        for rec in self:
            if rec.nota == 0:
                rec.estado_inscripcion = 'pendiente'
            if 0 < rec.nota < 4:
                rec.estado_inscripcion = 'libre'
            if 4 <= rec.nota < 6:
                rec.estado_inscripcion = 'regular'
            if rec.nota >= 6:
                rec.estado_inscripcion = 'aprobado'

    """
    @api.onchange('alumno_id, materia_id')
    def set_nombre_inscripcion(self):
        for inscripcion in self:
            if inscripcion.alumno_id and inscripcion.materia_id:
                inscripcion.nombre_inscripcion = inscripcion.alumno_id + ' - ' + inscripcion.materia_id
            else:
                inscripcion.nombre_inscripcion = ''
    """

    # Nota: crear modelo y vista de 'estado_inscripcion', y tomar de referencia
    # ./crm_aden_estudiante
