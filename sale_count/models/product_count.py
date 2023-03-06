from odoo import fields,models

class ProductCount(models.Model):
    _inherit = 'sale.order'

    product_count = fields.Integer()

    def action_confirm(self):
        res = super(ProductCount, self).action_confirm()
        for rec in self:
           rec.product_count = len(rec.order_line)
        return res


