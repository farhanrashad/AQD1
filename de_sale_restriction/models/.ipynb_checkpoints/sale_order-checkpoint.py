# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import datetime, time

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    @api.constrains('order_line')
    def _check_one_product_line(self):
        if len(self.order_line) > 1:
            raise UserError(_("You cannot confirm order '%s' because there is more than one product line.", self.name))
            

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    product_uom_qty = fields.Float(string='Quantity', digits='Product Unit of Measure', required=False, default=1.0)
