from odoo import models, fields, api, _


class DealerInformation(models.Model):
    _name = 'dealer.information'
    _description = 'dealer information description'
    _rec_name = 'first_name'

    first_name = fields.Char('First Name')
    last_name = fields.Char('Last Name')
    number = fields.Integer('Number')
    street = fields.Char('Street')
    city_id = fields.Many2one('res.city', string='City of Address')
    state_id = fields.Many2one('res.country.state', string='State of Address')
    country_id = fields.Many2one('res.country', string='Country' ,domain="['|',('code','=','CA'),('code','=','US')]")
    zip_code = fields.Integer('Zip code')

    @api.model
    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, '%s - %s' % (rec.first_name, rec.number)))
        return result

    count_dealer = fields.Integer(string='Count Dealer', compute='_compute_dealer_count')

    def _compute_dealer_count(self):
        for rec in self:
            count = self.env['regestration.information'].search_count([('dealer_id', '=', self.id)])
            rec.count_dealer = count

    def action_registration_class(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Dealer',
            'res_model': 'regestration.information',
            'domain': [('dealer_id', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
        }





