from odoo import models, fields, api, _


class ResCountryDemo(models.Model):
    _name = 'res.country.ksc'
    _description = 'Res country description'

    _sql_constraints = [('name_uniq', 'UNIQUE(short_code)', 'Code must be unique.')]

    name = fields.Char(string='Country Name')
    short_code = fields.Char(string='Short Code')
    state_ids = fields.One2many('res.state.ksc', 'country_id', string='state')



