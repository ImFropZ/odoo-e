from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    threshold = fields.Integer(
        string="Threshold",
        help="Set the threshold of the penalty.",
        config_parameter="hr_payroll_customized.threshold",
        default=0
    )

    deduced_amount = fields.Float(
        string="Deduced Amount",
        help="Set the deduced amount if employee count is more than threshold.",
        config_parameter="hr_payroll_customized.deduced_amount",
        default=0
    )

    @api.model
    def get_deduced_amount_from_settings(self):
        config_parameter_key = 'hr_payroll_customized.deduced_amount'
        deduced_amount = float(self.env['ir.config_parameter'].sudo(
        ).get_param(config_parameter_key, default=0))
        return deduced_amount

    @api.model
    def get_threshold_from_settings(self):
        config_parameter_key = 'hr_payroll_customized.threshold'
        threshold = float(self.env['ir.config_parameter'].sudo(
        ).get_param(config_parameter_key, default=0))
        return threshold
