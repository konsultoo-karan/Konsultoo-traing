from odoo import models, fields, api, _


class SaleOrderLineKsc(models.Model):
    _name = 'sale.order.line.ksc'
    _description = 'sale order line ksc description'

    order_id = fields.Many2one(comodel_name='sale.order.ksc', string='Order No')
    product_id = fields.Many2one(comodel_name='product.ksc', string='Product')
    name = fields.Text('Description')
    quantity = fields.Float('Quantity')
    unit_price  = fields.Float('Unit Price ')
    subtotal_without_tax = fields.Float('Subtotal Without Tax',compute='_compute_subtotal_without_tax',store=True)
    state = fields.Selection([('draft','Draft'),('confirmed','Confirmed'),('cancelled','Cancelled')])
    uom_id = fields.Many2one(comodel_name='product.uom.ksc',string='Unit of Measure')
    product_weight = fields.Float(related='product_id.weight')

    @api.onchange('product_id', 'sale_price')
    def _onchange_product_set_quantity(self):
        if self.product_id:
            self.unit_price = self.product_id.sale_price
            self.quantity = 1

    @api.depends('quantity','unit_price')
    def _compute_subtotal_without_tax(self):
        if self.product_id:
            self.subtotal_without_tax = self.quantity*self.unit_price
        else:
            self.subtotal_without_tax = 0




