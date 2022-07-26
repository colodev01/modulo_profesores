# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class EscuelaProfesor(models.Model):
    _name = 'escuela.profesor'

    nombre = fields.Char(string="Profesor", default="Jose Perez")
    edad = fields.Integer()
    legajo = fields.Char("Legajo")

    materia_id = fields.Many2many(
        comodel_name="escuela.materia", string="Materia"
    )

    # Implementar en metodo create() auto-incremento de variable legajo
    @api.constrains("legajo")
    def check_legajo(self):
        legajos = self.search([]).mapped("legajo")
        if self.legajo and self.legajo in legajos:
            raise exceptions.ValidationError("Existe legajo doble")
