from odoo import models, fields, api, _


class ResCityDemo(models.Model):
    _name = 'res.city.ksc'
    _description = 'Res city description'

    name = fields.Char(string='City Name')

    state = fields.Many2one('res.state.ksc', string='state')


    # console.log('hello ')


