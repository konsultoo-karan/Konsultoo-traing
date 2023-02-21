from odoo import models, fields, api, _


class ResStateDemo(models.Model):
    _name = 'res.state.ksc'
    _description = 'Res state description'

    name = fields.Char(string='Name')
    code = fields.Char(string='Short Code of the state')
    active = fields.Boolean(string='Active')

    country_id = fields.Many2one('res.country.ksc', string='Country Name')

    cities = fields.One2many('res.city.ksc','state', string='City')