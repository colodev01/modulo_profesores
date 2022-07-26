# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EscuelaMateria(models.Model):
    _name = 'escuela.materia'

    nombre = fields.Char(string="Materia")
    descripcion = fields.Text(string="Descripcion")

    profesor_id = fields.Many2many(
        comodel_name="escuela.profesor", string="Profesor"
    )
