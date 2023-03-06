from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    click_on_conform = fields.Integer(string="Product Count")


    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            order.click_on_conform = len(order.order_line)
        return res
