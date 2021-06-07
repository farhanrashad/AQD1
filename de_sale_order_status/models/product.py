# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import datetime, time

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    product_status = fields.Selection(
        [('0', 'Reserved'), ('1', 'Avaiable'), ('2', 'Not Avaiable')], string='Status', compute='_compute_product_status')
    
    def _compute_product_status2(self):
        for product in self:
            status = False
            quants = self.env['stock.quant'].search([('product_id.product_tmpl_id','=',product.id),('location_id.usage','=','internal')])
            for line in quants:
                if line.available_quantity > 0:
                    status = '2'
                elif line.available_quantity == 0:
                    status = '1'
                    
            if not status:
                status = '2'
            product.product_status = status
            
    def _compute_product_status(self):
        for product in self:
            sale_lines = self.env['sale.order.line'].search([('product_id.product_tmpl_id','=',product.id)])
            status = ''
            for line in sale_lines:
                if line.product_id:
                    if line.state == 'sale':
                        status = '0'
                    elif line.state in ('booked','done'):
                        status = '2'
                    else:
                        status = '1'
            if not status:
                status = '2'
            product.product_status = status