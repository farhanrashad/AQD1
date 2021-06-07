# -*- coding: utf-8 -*-

from odoo import models, fields, api , _
from odoo.exceptions import AccessError, UserError, ValidationError

class crmLead(models.Model):
    _inherit = 'crm.lead'
   
    #vat = fields.Char(related='partner_id.vat')
    vat = fields.Char(string='CNIC', )
    ref = fields.Char(string='Code')

    #_sql_constraints = [
    #    ('unique_vat_per_lead', 'unique (vat)', 'CNIC already registered with a lead/opportunity!'),
    #]
    
    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('crm.lead')
        return super(crmLead, self).create(vals)

    