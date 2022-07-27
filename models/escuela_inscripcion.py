# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EscuelaInscripcion(models.Model):
    _name = 'escuela.inscripcion'

    fecha_inscripcion = fields.Char(string="Materia")
    descripcion = fields.Text(string="Descripcion")

    alumno_id = fields.Many2one(
        comodel_name="escuela.alumno", string="Alumno"
    )
    materia_id = fields.Many2one(
        comodel_name="escuela.materia", string="Materia"
    )
    # Realizar vistas de modelo alumno, materia e inscripcion

