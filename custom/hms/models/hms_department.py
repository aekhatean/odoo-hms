from odoo import models, fields

class HmsDepartment(models.Model):
    _name = 'hms.department'
    _description = "Departments model"

    name = fields.Char()
    capacity = fields.Float()
    is_opened = fields.Boolean()
    patients_ids = fields.One2many(comodel_name='hms.patient', inverse_name="department_id")