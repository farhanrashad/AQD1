# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, ValidationError

        
class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    vat = fields.Char(string='CNIC', index=True, )
