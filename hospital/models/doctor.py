
from odoo import api, models, fields
from odoo.exceptions import ValidationError, UserError

class HospitalDoctorSkill(models.Model):
    _name = "hospital.doctor.skill"
    _description = "Hospital Doctor Skill"

    name = fields.Char(string='Name', required=True)

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "Hospital Doctor Details"

    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone', required=True)
    age = fields.Integer(string='Age', copy=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')
    active = fields.Boolean(string="Active", default=True)
    skill_ids = fields.Many2many('hospital.doctor.skill', string="Skill")

    @api.constrains('phone')
    def _check_phone_constraint(self):
        for doctor in self:
            if len(doctor.phone) > 4:
                raise UserError('The phone must be four digit!')
            domain = [('id', '!=', doctor.id), ('name', '=', doctor.name)]
            if self.search(domain):
                raise ValidationError('The name must be unique!')
