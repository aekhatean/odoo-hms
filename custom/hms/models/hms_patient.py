from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError, UserError
from datetime import date


# eng.mohammedashraf96@gmail.com
class HmsPatient(models.Model):
    _name = "hms.patient"
    _rec_name = "first_name"
    _description = "Patients model"

    first_name = fields.Char()
    last_name = fields.Char()
    email = fields.Char()
    birth_date = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    state = fields.Selection(
        [
            ('Undetermined', 'undetermined'),
            ('Good', 'good'),
            ('Fair', 'fair'),
            ('Serious', 'serious'),
        ],
        default="Undetermined"
    )
    blood_type = fields.Selection(
        [
            ('O+', 'O+'),
            ('O-', 'O-'),
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
        ],
        default="O-"
    )
    age = fields.Integer(compute='_compute_age')
    pcr = fields.Boolean()
    image = fields.Image()
    address = fields.Text()
    department_id = fields.Many2one(comodel_name='hms.department')
    doctors_ids = fields.Many2many(comodel_name='hms.doctor')
    customer_id = fields.Many2one(comodel_name="res.partner")
    logs = fields.One2many(comodel_name='hms.patient_log')

    _sql_constraints = [
        ('UNIQUE_EMAIL_CONSTRAINT', 'unique(email)', 'This email already exists')
    ]

    @api.onchange('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                rec.age = date.today().year - rec.birth_date.year
            else:
                rec.age = 0

    @api.onchange('birth_date')
    def _age_pcr_checker(self):
        if self.age < 30:
            self.pcr = True
        return {
            'warning': {
                'title': "PCR checked",
                'message': "Checked PCR because patient's age is less 30"
            }
        }

    @api.onchange('email')
    def _email_validator(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if len(self.email) > 0:
            match = re.fullmatch(regex, self.email)
            if match is None:
                raise ValidationError('Not a valid E-mail ID.')

    @api.onchange('state')
    def _state_logger(self):
        self.env['hms.patient_log'].create({'desc': "A change made to this patient's state", 'patient_id': self.id})