from odoo import models, fields


class SaleOrderKsc(models.Model):
    _inherit = 'sale.order'
    _description = 'sale order information'

    count_total = fields.Char(string="Count Total Order")

    def action_confirm(self):
        res = super(SaleOrderKsc, self).action_confirm()
        for record in self:
            record.count_total = len(record.order_line)
        return res
