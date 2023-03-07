from odoo import models, fields, api, _


class RegestrationInformation(models.Model):
    _name = 'regestration.information'
    _description = 'regestration information description'
    _rec_name = 'reg_card_number'

    dealer_id = fields.Many2one('dealer.information',required=True, string='Dealer')
    first_name = fields.Char('First Name')
    last_name = fields.Char('Last Name')
    street = fields.Char('Street')
    city_id = fields.Many2one('res.city', string='City of Address')
    state_id = fields.Many2one('res.country.state', string='State of Address')
    country_id = fields.Many2one('res.country', string='Country')
    reg_card_number = fields.Integer('Registration Card Number',required=True)
    email = fields.Char('Email')
    purchase_date = fields.Date('Date')
    dot_id_1 = fields.Char('Dot id 1')
    qty_1 = fields.Integer('Qty 1')
    dot_id_2 = fields.Char('Dot id 2')
    qty_2 = fields.Integer('Qty 2')
    dot_id_3 = fields.Char('Dot id 3')
    qty_3 = fields.Integer('Qty 3')
    dot_id_4 = fields.Char('Dot id 4')
    qty_4 = fields.Integer('Qty 4')
    dot_id_5 = fields.Char('Dot id 5')
    qty_5 = fields.Integer('Qty 5')
    dot_id_6 = fields.Char('Dot id 6')
    qty_6 = fields.Integer('Qty 6')
    model_name = fields.Char('Model Name')
    vin = fields.Char('Vin')
    year = fields.Char('Year', size=4)
    enter_date = fields.Datetime('Enter Date and Time')
    user_id = fields.Many2one('res.users','Users')

    _sql_constraints = [('name_uniq', 'UNIQUE(reg_card_number)', 'Reg card number must be unique.')]

    @api.onchange('dealer_id')
    def _onchange_on_dealer_id(self):
        if self.dealer_id:
            self.state_id = self.dealer_id.state_id
            self.city_id = self.dealer_id.city_id
            self.country_id = self.dealer_id.country_id



