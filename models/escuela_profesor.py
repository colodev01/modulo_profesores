# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class EscuelaProfesor(models.Model):
    _name = 'escuela.profesor'
    _description = 'Profesores'

    nombre = fields.Char(string="Profesor", default="Jose Perez")
    edad = fields.Integer()
    legajo = fields.Integer()

    materia_id = fields.Many2many(
        comodel_name="escuela.materia", string="Materia"
    )

    def get_nuevo_legajo(self):
        ultimo_profesor = self.env["escuela.profesor"].search([], order="id desc", limit=1)
        nuevo_legajo = ultimo_profesor.legajo + 1 if ultimo_profesor else 1
        return nuevo_legajo
        """
        profesores = self.env["escuela.profesor"].search([], order="id desc", limit=1)
        legajoAlto=0
        if len(profesores)>0:
            for i in range(len(profesores)):
                if legajoAlto < profesores[i].legajo:
                    legajoAlto = profesores[i].legajo
        return legajoAlto+1
        """


    @api.model
    def create(self, values):
        values['legajo'] = self.get_nuevo_legajo()
        record = super(EscuelaProfesor, self).create(values)
        return record

    """
    @api.constrains("legajo")
    def check_legajo(self):
        legajos = self.search([]).mapped("legajo")
        if self.legajo and self.legajo in legajos:
            raise exceptions.ValidationError("Existe legajo doble")
    """
