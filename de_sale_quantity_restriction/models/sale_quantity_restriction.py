# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import datetime
import calendar



class SaleOrderInherit(models.Model):
    _inherit = "sale.order.line"
    
    
    
    product_id = fields.Many2one('product.product', string='Product',  domain="([('qty_available' , '>' , 0)])")