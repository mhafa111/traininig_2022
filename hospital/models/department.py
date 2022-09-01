from odoo import models, fields

class Department(models.Model):
    _name = "department.doctor"
    _description = "Hospital Doctor Department"
    _rec_name ='department'

    department = fields.Char(string='Department', required=True)
    manger = fields.Char(string='Manger', required=True)
    #doctor_id = fields.One2many('hospital.doctor' , 'Doctor')

