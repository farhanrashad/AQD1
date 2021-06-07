# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    dealers = fields.Many2many (related='team_id.dealer_id')
    dealer_id = fields.Many2one('res.partner',  domain="[('id','in', dealers)]",required=True, string="Dealer",)
    
    def action_confirm(self):
        rec = super(SaleOrder, self).action_confirm()
        vals = {
            'sale_id':self.id,        
        }
        self.env['sale.dealer.commission.line'].create(vals)
        return rec
    
    
    