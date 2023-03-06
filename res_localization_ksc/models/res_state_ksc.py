from odoo import api,fields,models
from odoo.exceptions import ValidationError


class ResStateKsc(models.Model):
    _name = "res.state.ksc"

    name = fields.Char(string="Name of State")
    state_code = fields.Char(string="Short code of state")

    country_id = fields.Many2one('res.country.ksc')

    cities_ids = fields.One2many('res.city.ksc','state_list_id',string="City list")

    _sql_constraints = [
        ('unique_state_code', 'unique(state_code)', 'The state code must be unique!')
    ]


    @api.constrains('state_code')
    def _check_unique_state_code(self):
        for record in self:
            if record.state_code and self.search_count([('state_code', '=', record.state_code)]) > 1:
                raise ValidationError('State code must be unique')






