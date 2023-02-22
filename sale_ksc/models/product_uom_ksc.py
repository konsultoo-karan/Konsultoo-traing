from odoo import models, fields, api, _


class ProductUom(models.Model):
    _name = 'product.uom.ksc'
    _description = 'product uom ksc description'

    name = fields.Char(string='Uom Name')
    uom_category_id = fields.Many2one('product.uom.category.ksc','Uom Category')
