from odoo import models, fields


class HmsPatient(models.Model):
    _name = "hms.doctor"
    _rec_name = "first_name"
    _description = "Doctors model"

    first_name = fields.Char()
    last_name = fields.Char()
    image = fields.Image()
    patients_ids = fields.Many2many(comodel_name='hms.patient')