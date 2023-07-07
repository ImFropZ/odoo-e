from odoo import http
from odoo.http import request


class DonationController(http.Controller):
    @http.route('/donation/process_payment', type='json', auth='public', website=True)
    def process_payment(self, donation_id, **kwargs):
        donation = request.env['custom_donation.donation'].sudo().browse(
            int(donation_id))
        amount = donation.amount

        # Call the payment provider's API or perform the necessary payment processing here
        # You will need to implement the specific integration with your payment provider

        # Example: Simulate a successful payment
        donation.write({'state': 'paid'})
        return {'result': 'success', 'message': 'Payment successful'}

    @http.route('/donation/cancel_payment', type='json', auth='public', website=True)
    def cancel_payment(self, donation_id, **kwargs):
        donation = request.env['custom_donation.donation'].sudo().browse(
            int(donation_id))

        # Perform any necessary actions to handle a canceled or failed payment
        # This can include updating the donation state or performing any required cleanup

        # Example: Simulate a canceled payment
        donation.write({'state': 'canceled'})
        return {'result': 'success', 'message': 'Payment canceled'}

    @http.route('/donation/payment', type='http', auth='public', website=True)
    def donation_payment(self, donation_id, **kwargs):
        donation = request.env['custom_donation.donation'].sudo().browse(
            int(donation_id))

        return request.render('custom_donation.donation_payment', {
            'publishable_key': 'pk_test_TYooMQauvdEDq54NiTphI7jx',
            'donation_id': donation_id
        })
