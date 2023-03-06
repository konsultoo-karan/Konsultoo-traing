from odoo import fields, models

class ResCityKsc(models.Model):
    _name = 'res.city.ksc'
    _description = 'City Information'
    _rec_name = 'city_name'

    city_name = fields.Char(string='Name of the City')

    state_id = fields.Many2one('res.state.ksc', string='State')