from odoo import models, fields, api, _


class SaleOrderKsc(models.Model):
    _name = 'sale.order.ksc'
    _description = 'sale order ksc description'

    name = fields.Char(string='Order No')
    customer_id = fields.Many2one('res.partner.ksc')
    invoice_id = fields.Many2one('res.partner.ksc')
    shiping_id = fields.Many2one('res.partner.ksc')
    sale_order_date = fields.Date('Sale Order Date')
    # order_line_ids = fields.One2many('sale.order.line.ksc')
    user_id = fields.Many2one('res.users', string='Salesperson')
    state_data = [('draft', 'Draft'),('confirmed', 'Confirmed'),('done', 'Done'),('cancelled', 'Cancelled')]
    state = fields.Selection(selection=state_data, string='State', default='draft')
