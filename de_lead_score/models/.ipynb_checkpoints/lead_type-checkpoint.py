# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class crmLeadType(models.Model):
    _name = 'crm.lead.type'
    _description = 'crm lead type'
    
    
    name = fields.Char(string="Lead Type", required=True)
    value = fields.Float(string="Value", required=True)
    min_value = fields.Float(string="Minimum", required=True)
    max_value = fields.Float(string="Maximum", required=True)
    convert_opportunity = fields.Boolean(string='Convert into opportunity')
    
    @api.onchange('value')
    def _onchange_value(self):
        if self.value:
            self.min_value = self.value
    