from odoo import models, fields


class HmsPatientLog(models.Model):
    _name = "hms.patient"
    _rec_name = "first_name"
    _description = "Patients model"

    desc = fields.Char()
