# -*- coding: utf-8 -*-

from odoo import models, fields


class EscuelaProfesor(models.Model):
    _name = 'escuela.profesor'

    nombre = fields.Char(string="Profesor")
    edad = fields.Integer()

