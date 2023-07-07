from odoo import models, fields


class Donation(models.Model):
    _name = 'custom_donation.donation'
    _description = 'Donation'

    donor_name = fields.Char(string='Donor Name')
    amount = fields.Float(string='Amount')
    donation_date = fields.Date(string='Donation Date')
    payment_method = fields.Selection(
        [('cash', 'Cash'), ('credit_card', 'Credit Card')],
        string='Payment Method'
    )
    status = fields.Selection(
        [("processing", "Processing"), ("paid", "Paid"), ("canceled", "Canceled")], string="Status", deafult="processing")
