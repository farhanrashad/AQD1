# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime, timedelta
from functools import partial
from itertools import groupby

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.misc import formatLang, get_lang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare



from werkzeug.urls import url_encode


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Reserved'),
         ('booked', 'Booking Confirmed'),
        ('done', 'Locked'),
        ('cancel', 'Booking Cancel'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    
    def action_booking_confirm(self):
        self.write({
            'state':'booked',
        })
        