from odoo import fields, models

class ResCountryKsc(models.Model):
    _name = 'res.country.ksc'
    _description = 'Country Information'
    _rec_name = 'country_name'

    country_name = fields.Char(string='Name of the Country')
    country_code = fields.Char(string='Short Code Of the country')

    states_ids = fields.One2many('res.state.ksc', 'country_id', string='state')

    _sql_constraints = [
        ('country_code_uniq', 'unique (country_code)', 'country codes must be unique per country.'),
    ]