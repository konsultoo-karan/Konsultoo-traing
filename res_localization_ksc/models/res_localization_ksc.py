from odoo import fields, models, api
from odoo.exceptions import ValidationError

class ResCountryKsc(models.Model):
    _name = "res.country.ksc"
    _description = 'Country KSC'

    name = fields.Char("Name of the country")
    code = fields.Char("Short Code of the country")
    state_ids = fields.One2many(comodel_name='res.state.ksc', inverse_name='country_id', string='States')


    _sql_constraints = [
        ('unique_code', 'unique(code)', 'The Country code must be unique!'),
    ]



class ResStateKsc(models.Model):
    _name = 'res.state.ksc'
    _description = 'State KSC'

    name = fields.Char(string='Name of the state', required=True)
    code = fields.Char(string='Short Code of the state', required=True)
    country_id = fields.Many2one(comodel_name='res.country.ksc', string='Country', required=True)

    city_ids = fields.One2many(comodel_name='res.city.ksc', inverse_name='state_id', string='Cities')

    @api.constrains('code')
    def _check_code(self):
        if self.code and self.env['res.state.ksc'].search_count([('code', '=', self.code)]) > 1:
            raise ValidationError('The Code Must Be Unique....!!!!')

class ResCityKsc(models.Model):
    _name = 'res.city.ksc'
    _description = 'City KSC'

    name = fields.Char(string='City Name', required=True)
    state_id = fields.Many2one(comodel_name='res.state.ksc', string='State', required=True)

# class TestyKscInherit(models.Model):
#     _inherit = 'res.partner'
#     _description = 'check inherits'
#     test1 = fields.Char("Test henherit")
#
# class TestyKsc(models.Model):
#     _name = 'test.hinherits'
#     _inherits = {'res.partner': 'partner_id'}
#     _description = 'check inherits'

