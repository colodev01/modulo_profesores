# -*- coding: utf-8 -*-

from odoo import models, fields


class EscuelaInscripcion(models.Model):
    _name = 'escuela.inscripcion'

    nota = fields.Float(string="Nota final", default=0)
    fecha_inscripcion = fields.Date(string="Fecha de Inscripcion")

    alumno_id = fields.Many2one(
        comodel_name="escuela.alumno", string="Alumno"
    )
    materia_id = fields.Many2one(
        comodel_name="escuela.materia", string="Materia"
    )

    # Nota: crear modelo y vista de 'estado_inscripcion', y tomar de referencia
    # ./crm_aden_estudiante



