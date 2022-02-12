from odoo import models, fields, api
from odoo.exceptions import UserError


class HmsInheritCustomers(models.Model):
    _inherit = 'res.partner'
    related_patient_id = fields.Many2one(comodel_name="hms.patient")

    @api.onchange('email')
    def _patient_customer_non_crossing_validation(self):
        if self.env['hms.patient'].search([('email', '=', self.email)]):
            raise UserError('Patient email and customer email cannot be the same.')

    @api.constrains('related_patient_id')
    def _check_related_patients(self):
        for rec in self:
            if len(rec.related_patient_id) > 0:
                raise UserError('You cannot delete customer with related patient(s)')