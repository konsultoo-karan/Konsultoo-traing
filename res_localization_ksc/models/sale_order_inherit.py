from odoo import models, fields, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_line_count = fields.Char(string="Order Line Count")

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        print('Res ::::::::::::::::: = True',res)

        for record in self:
            record.order_line_count = len(record.order_line)
        return res






