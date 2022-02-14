from odoo import models, fields


class HmsPatientLog(models.Model):
    _name = "hms.patient_log"
    _rec_name = "first_name"
    _description = "Patients model"

    desc = fields.Char()
    patient_id = fields.Many2one(comodel_name='hms.patient')
