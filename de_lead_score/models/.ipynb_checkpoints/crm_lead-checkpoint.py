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


score_points = [
    [0.30, 0.60, 0.90, 1.20, 1.5],
    [0.25, 0.50, 0.75, 1.00, 1.25],
    [0.15, 0.30, 0.45, 0.60, 0.75],
    [0.10, 0.20, 0.30, 0.40, 0.5],
    [0.20, 0.40, 0.60, 0.80, 1],
]


class CrmLead(models.Model):
    _inherit = 'crm.lead' 
    
    lead_scoring_ids = fields.One2many('crm.lead.score', 'opportunity_id')
    
    lead_score = fields.Float(string="Lead Score", readonly=True, compute='_lead_score')
    is_opportunity = fields.Boolean()
    bad = fields.Float(string="Bad", readonly=True, compute='_lead_score')
    unfair = fields.Float(string="Unfair", readonly=True, compute='_lead_score')
    fair = fields.Float(string="Fair", readonly=True, compute='_lead_score')
    good = fields.Float(string="Good", readonly=True, compute='_lead_score')
    excellent = fields.Float(string="Excellent", readonly=True, compute='_lead_score')
    
    total = fields.Float(string="Total", compute="_lead_score_total", default=0.0)
    max_score = fields.Float(string="Max Score", default=0.0, compute='_lead_score_total')
    min_score = fields.Float(string="Min Score", default=0.0, compute='_lead_score_total')
    
    lead_type = fields.Many2one('crm.lead.type',string="Lead Type", compute='_compute_lead_type')

    @api.depends('lead_scoring_ids','total')
    def _compute_lead_type(self):
        for lead in self:
            lead_type = self.env['crm.lead.type'].search([('min_value','<=', lead.total),('max_value','>=', lead.total)],limit=1)
            lead.update({
                'lead_type':lead_type.id,
            })


    @api.depends('lead_scoring_ids', 'lead_scoring_ids.weightage', 'lead_scoring_ids.scale')
    def _lead_score_total(self):
        score_list = []
        tot = scale = 0.0
        for lead in self:
            tot = 0.0
            for line in lead.lead_scoring_ids:
                scale = float(line.scale)
                score_list.append(scale)
                tot += (float(line.scale))
            if len(score_list):
                lead.update({
                    'max_score':max(score_list),
                    'min_score':min(score_list),
                    'total':tot
                })
            else:
                lead.update({
                    'max_score':0,
                    'min_score':0,
                    'total':0,
                })
           
    @api.depends('lead_scoring_ids', 'lead_scoring_ids.weightage', 'lead_scoring_ids.scale')
    def _lead_score(self):

        bad = 0.00
        unfair = 0.00
        fair = 0.00
        good = 0.00
        excellent = 0.00

        sore_list = []

        ind = 0
        try:
            for rec in self.lead_scoring_ids:
                scale = int(rec.scale)
                if scale == 0:
                    bad = bad + score_points[ind][scale]
                    sore_list.append(score_points[ind][scale])
                elif scale == 1:
                    unfair = unfair + score_points[ind][scale]
                    sore_list.append(score_points[ind][scale])
                elif scale == 2:
                    fair = fair + score_points[ind][scale]
                    sore_list.append(score_points[ind][scale])
                elif scale == 3:
                    good = good + score_points[ind][scale]
                    sore_list.append(score_points[ind][scale])
                elif scale == 4:
                    excellent = excellent + score_points[ind][scale]
                    sore_list.append(score_points[ind][scale])
                ind = ind + 1
        except:
            pass

        self.bad = bad
        self.unfair = unfair
        self.fair = fair
        self.good = good
        self.excellent = excellent
        self.total = bad + unfair + fair + good + excellent
        self.lead_score = self.total
        if self.total > 1.00:
            self.is_opportunity = True
        else:
            self.is_opportunity = False
        try:
            self.max_score = max(sore_list)
            self.min_score = min(sore_list)
            #self.max_score = self.min_score = 10
        except:
            pass
    
    
    @api.model
    def default_get(self,  default_fields):
        res = super(CrmLead, self).default_get(default_fields)
        lead_scores = self.env['crm.lead.score.default'].search([])
        lead_data = []
        for score in lead_scores:
            lead_data.append((0,0,{
                'lead_score_type_id': score.lead_score_type_id.id,
                'weightage': score.weightage,
                'scale': '0',
            }))
        self.lead_scoring_ids = lead_data
        return res
    
    #@api.onchange('name')
    def onchange_name(self):
        if self.total > 1.00:
            self.is_opportunity = True
        else:
            self.is_opportunity = False
            
        if not self.name:
            for other_input in self.lead_scoring_ids:
                other_input.unlink()
            score_list = []
            data = []

            lead_scores = self.env['crm.lead.score.default'].search([])
            for score in lead_scores:
                data.append((0,0,{
                            'lead_score_type_id': score.lead_score_type_id.id,
                            'weightage': score.weightage,
                            }))
            self.lead_scoring_ids = data 


class crmLeadScore(models.Model):
    _name = 'crm.lead.score'
    _description = 'crm lead scoring'
    lead_score_type_id = fields.Many2one('crm.lead.score.type', string='Score Type', required=True)
    weightage = fields.Float(string='Weightage (%)', digits='Discount', default=0.0, required=True)
    scale = fields.Selection([
        
        ('4' , 'Excellent'),
        ('3', 'Good'),
        ('2', 'Fair'),
        ('1', 'Unfair'),
        ('0', 'Bad'),
    ], string="Scale",default='0', required=True)
    opportunity_id = fields.Many2one('crm.lead', required=True)
