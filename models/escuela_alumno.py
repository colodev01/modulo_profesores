# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class EscuelaAlumno(models.Model):
    _name = 'escuela.alumno'

    nombre = fields.Char(string="Alumno", default="Fernando Rodriguez")
    edad = fields.Integer()


