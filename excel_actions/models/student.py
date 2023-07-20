from odoo import fields, api, models


class ExcelStudent(models.Model):
    _name = "excel.student"

    name = fields.Text(string="Fullname")
    age = fields.Integer(string="Age")
