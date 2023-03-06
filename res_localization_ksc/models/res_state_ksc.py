from odoo import models, fields, api, _


class ResStateDemo(models.Model):
    _name = 'res.state.ksc'
    _description = 'Res state description'

    _sql_constraints = [('name_uniq', 'UNIQUE(code)', 'Code must be unique.')]

    name = fields.Char(string='Name')
    code = fields.Char(string='Short Code of the state')
    active = fields.Boolean(string='Active')

    country_id = fields.Many2one('res.country.ksc', string='Country Name')

    cities = fields.One2many('res.city.ksc','state', string='City')