# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class EscuelaProfesor(models.Model):
    _name = 'escuela.profesor'

    nombre = fields.Char(string="Profesor", default="Jose Perez")
    edad = fields.Integer()
    legajo = fields.Integer()

    materia_id = fields.Many2many(
        comodel_name="escuela.materia", string="Materia"
    )

    def getHighestLegajo(self):
        profesores = self.env["escuela.profesor"].search([])
        legajoAlto=0
        if len(profesores)>0:
            for i in range(len(profesores)):
                if legajoAlto < profesores[i].legajo:
                    legajoAlto = profesores[i].legajo
        return legajoAlto+1

    @api.model
    def create(self, values):
        values['legajo'] = self.getHighestLegajo()
        record = super(EscuelaProfesor, self).create(values)
        return record

    """
    @api.constrains("legajo")
    def check_legajo(self):
        legajos = self.search([]).mapped("legajo")
        if self.legajo and self.legajo in legajos:
            raise exceptions.ValidationError("Existe legajo doble")
    """