from odoo import models, fields, api




class LibraryBook(models.Model):
    _name = 'product.category.ksc'
    _description = 'product category'

    name = fields.Char('Name')
    parent_id = fields.Many2one('product.ksc', string='Parent')

