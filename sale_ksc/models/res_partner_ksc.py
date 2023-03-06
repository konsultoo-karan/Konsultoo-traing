from odoo import models, fields, api, _


class ResPartnerKsc(models.Model):
    _name = 'res.partner.ksc'
    _description = 'res partner description'

    name = fields.Char(string='Partner Name')
    street_1 = fields.Char(string='Street 1')
    street_2 = fields.Char(string='Street 2')
    country_id = fields.Many2one('res.country.ksc',string='Country')
    state_id = fields.Many2one('res.state.ksc',string='State')
    city_id = fields.Many2one('res.city.ksc',string='City')
    zip_code = fields.Char(string='Zip Code')
    email = fields.Char(string='Email')
    mobile = fields.Char(string='Mobile')
    phone = fields.Char(string='Phone')
    photo = fields.Image(string='Photo')
    website = fields.Char(string='Website')
    active = fields.Boolean('Active')
    parent_id = fields.Many2one('res.partner.ksc',string='Parent')
    child_ids = fields.One2many('res.partner.ksc','parent_id',string='Child')
    address_type = fields.Selection([('invoice', 'Invoice'), ('shipping', 'Shipping'), ('contact', 'Contact')],string='Address Type')

    def name_get(self):
        result = []

        for rec in self:
            print('\nrec :::::::',rec)
            print('\n\nself ::::::::::',self)
            result.append((rec.id, '%s - %s' % (rec.email, rec.name)))
        return result

    # @api.model
    # def name_search(self,name, args=None, operator='ilike',limit=100):
    #     args = args or []
    #     if name:
    #         records = self.search(['|','|',('name',operator,name),('email',operator,name),('street_1',operator,name)])
    #         return records.name_get()
    #     return self.search([('name',operator,name)] + args, limit=limit).name_get()