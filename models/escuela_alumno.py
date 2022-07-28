# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EscuelaAlumno(models.Model):
    _name = 'escuela.alumno'
    _rec_name = 'nombre_completo'

    nombre = fields.Char(string="Nombre")
    apellido = fields.Char(string="Apellido")
    edad = fields.Integer()
    nombre_completo = fields.Char(string="Apellido y nombre", compute="set_full_name")

    @api.onchange('nombre', 'apellido')
    def set_full_name(self):
        for estudiante in self:
            if estudiante.nombre and estudiante.apellido:
                estudiante.nombre_completo = str(estudiante.apellido) + ', ' + str(estudiante.nombre)
            else:
                estudiante.nombre_completo = ''

    """
    def name_get(self):
       res = []
       for record in self:
           nombre_completo = str(record.apellido) + ', ' + str(record.nombre)
           res.append((record.id, nombre_completo))
       return res
   """