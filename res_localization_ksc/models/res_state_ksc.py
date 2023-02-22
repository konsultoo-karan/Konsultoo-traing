from odoo import api, fields, models

class Resstate(models.Model):
        _name = 'res.state.ksc'
        _description = 'state information'


        name = fields.Char(string="Name Of State")
        code= fields.Char(string="Code of the State")
        country_id = fields.Many2one(comodel_name='res.country', string='State Name ')
        # city_ids = fields.One2many('(res.city.ksc', 'state_id', string='City')


        # Cities - One2many(res.city.ksc)