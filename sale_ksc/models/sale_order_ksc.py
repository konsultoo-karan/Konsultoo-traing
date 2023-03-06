from odoo import models, fields, api, _


class SaleOrderKsc(models.Model):
    _name = 'sale.order.ksc'
    _description = 'sale order ksc description'

    name = fields.Char(string='Order No')
    partner_id = fields.Many2one('res.partner.ksc')
    invoice_id = fields.Many2one('res.partner.ksc')
    shiping_id = fields.Many2one('res.partner.ksc')
    sale_order_date = fields.Date('Sale Order Date')
    order_line_ids = fields.One2many(comodel_name='sale.order.line.ksc', inverse_name='order_id', string='Order Line')
    user_id = fields.Many2one('res.users', string='Salesperson')
    state_data = [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done'), ('cancelled', 'Cancelled')]
    state = fields.Selection(selection=state_data, string='State', default='draft')

    total_weight = fields.Float('Total Weight', compute='compute_weight', store=False)
    total_volume = fields.Float('Total Volume', compute='_compute_volume', store=False)
    order_total = fields.Float('Total Order',compute='',store=True)


    @api.depends('order_line_ids')
    def compute_weight(self):
        total_weights = []
        self.total_weight = 0
        for rec in self.order_line_ids:
            total_w = rec.quantity * rec.product_id.weight
            if total_w:
                total_weights.append(total_w)
        self.total_weight = sum(total_weights)

    @api.depends('order_line_ids')
    def _compute_volume(self):
        total_volume = []
        self.total_volume = 0
        for rec in self.order_line_ids:
            total_v = rec.quantity * rec.product_id.volume
            if total_v:
                total_volume.append(total_v)
        self.total_volume = sum(total_volume)







        # @api.depends('order_line_ids.quantity','order_line_ids.product_weight')
        # def _compute_total_weight(self):
        #     for rec in self:
        #         rec.total_weight = 0
        #         for order in rec.order_line_ids:
        #             if order.product_weight:
        #                 rec.total_weight += sum([order.quantity * order.product_weight])

