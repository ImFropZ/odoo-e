from odoo import fields, api, models


class HrPayslipCustomized(models.Model):
    _inherit = "hr.payslip"

    count = fields.Integer(string="Count", readonly=True)

    @api.onchange("employee_id", "date_from", "date_to")
    def _on_change_count(self):
        hr_attendance_obj = self.env["hr.attendance"]
        attendance_records = hr_attendance_obj.search([
            '|',
            '&',
            ('check_in', '>=', self.date_from),
            ('employee_id', '=', self.employee_id.id),
            '&',
            ('check_out', '<=', self.date_to),
            ('employee_id', '=', self.employee_id.id),
        ])

        self.count = sum(attendance_records.mapped('count'))
