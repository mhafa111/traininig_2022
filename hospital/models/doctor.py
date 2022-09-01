
from odoo import models, fields

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "Hospital Doctor Details"
    _rec_name ='name'


    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', copy=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], required=True, default='male')
    note = fields.Text(string='Description')
    active = fields.Boolean(string="Active", default=True)
    image = fields.Binary(string='Image Doctor')
    department_id = fields.Many2one('department.doctor' , 'Department')
    manger_de = fields.Char(string='Manger Department', related='department_id.manger')
    

