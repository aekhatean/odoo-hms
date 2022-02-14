from odoo import models, fields, api
from odoo.exceptions import UserError


class HmsInheritCustomers(models.Model):
    _inherit = 'res.partner'
    related_patient_id = fields.Many2one(comodel_name="hms.patient")

    @api.onchange('email')
    def _patient_customer_non_crossing_validation(self):
        if self.env['hms.patient'].search([('email', '=', self.email)]):
            raise UserError('Patient email and customer email cannot be the same.')

    def unlink(self):
        for rec in self:
            if rec.related_patient_id:
                raise UserError('You cannot delete customer with related patient(s)')