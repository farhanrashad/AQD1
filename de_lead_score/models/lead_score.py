# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class crmLeadScoreType(models.Model):
    _name = 'crm.lead.score.type'
    _description = 'crm lead score type'
    
    name = fields.Char(string="Factor", required=True)
    
class crmLeadScoreDefault(models.Model):
    _name = 'crm.lead.score.default'
    _description = 'crm lead score Default'
    
    lead_score_type_id = fields.Many2one('crm.lead.score.type', string='Score Type', required=True)
    weightage = fields.Float(string='Weightage (%)', digits='Discount', default=0.0, required=True)


    @api.constrains('weightage')
    def calculate_weightage(self):
        total_weightage = 0.00
        rec = self.search([])
        for r in rec:
            total_weightage = total_weightage + (r.weightage) * 100
        if total_weightage > 100:
            raise UserError(('Sorry ! Weightage can not be greater than 100'))

