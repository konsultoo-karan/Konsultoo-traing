from odoo import models, fields, api, _


class ProductResDemo(models.Model):
    _name = 'product.ksc'
    _description = 'product ksc description'

    name = fields.Char(string='Product Name')
    sku = fields.Char(string='Sku')
    weight = fields.Float(string='Weight')
    length = fields.Float(string='length')
    barcode = fields.Char(string='Barcode')

    product_type = fields.Selection([('storable','Storable'),('consumable','Consumable'),('service','Service')], string='Product Type')

    sale_price = fields.Float('Sale Price')
    cost_price = fields.Float('Cost Price')
    product_category_id = fields.Many2one('product.category.ksc')
    uom_id = fields.Many2one('product.uom.ksc',string='UOM')


