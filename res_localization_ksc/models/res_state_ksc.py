from odoo import fields, models,api
from odoo.exceptions import ValidationError


class ResStateKsc(models.Model):
    _name = 'res.state.ksc'
    _description = 'State Information'
    _rec_name = 'state_name'

    state_name = fields.Char(string='Name of the State')
    state_code = fields.Char(string='Short Code Of the State')

    country_id = fields.Many2one('res.country.ksc', string='Country')
    cities_ids = fields.One2many('res.city.ksc', 'state_id', string='City')

    @api.constrains('state_code')
    def _check_uniq_code(self):
        for rec in self:
            if rec.state_code and self.search_count([('state_code', '=', rec.state_code)])>1:
                raise ValidationError("State Code must be different")
