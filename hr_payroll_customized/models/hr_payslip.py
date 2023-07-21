from dateutil.relativedelta import relativedelta
from odoo import fields, api, models


class HrPayslipCustomized(models.Model):
    _inherit = "hr.payslip"

    count = fields.Integer(string="Count", readonly=True,
                           compute="_compute_count")
    paid_amount = fields.Float(
        string="Paid Amount", readonly=True, store=True)

    @api.depends("employee_id", "date_from", "date_to")
    def _compute_count(self):
        if not self.employee_id:
            self.count = 0
            return

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

        # Getting threshold and deduced amount from settings
        settings = self.env['res.config.settings'].create({})
        setting_threshold = settings.get_threshold_from_settings()
        setting_deduced_amount = settings.get_deduced_amount_from_settings()

        print(setting_threshold, setting_deduced_amount)

        self.paid_amount = sum(
            self.worked_days_line_ids.mapped("amount")
        ) - (
            (self.count % setting_threshold) * setting_deduced_amount
        )
