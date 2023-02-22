from odoo import models, fields, api, _


class ProductUomksc(models.Model):
    _name = 'product.uom.category.ksc'
    _description = 'product ksc description'

    name = fields.Char(string='Category Name')
    uom_ids = fields.One2many('product.uom.ksc','uom_category_id',string='Uom ids')