from odoo import fields,models

class ResStateKsc(models.Model):

    _name = 'res.city.ksc'

    name = fields.Char(string="City name")

    state_list_id = fields.Many2one('res.state.ksc', string="State List")