# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError, ValidationError

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    @api.constrains('stage_id', 'checklist_progress')
    def _check_constrains_won_opportunity(self):
        if self.stage_id.is_won and self.checklist_progress < 100:
            raise UserError(_('Opportunity could not won with incomplete checklist'))

                
    @api.depends('crm_checklist_ids')
    def checklist_progress(self):
        total_len = self.env['crm.checklist'].search_count([])
        for rec in self:
            if total_len != 0:
                check_list_len = len(rec.crm_checklist_ids)
                rec.checklist_progress = (check_list_len * 100) / total_len
            else:
                rec.checklist_progress = 0

    crm_checklist_ids = fields.Many2many('crm.checklist', string='Check List')
    checklist_progress = fields.Float(compute=checklist_progress, string='Progress', store=True,
                                      default=0.0)
    max_rate = fields.Integer(string='Maximum rate', default=100)


class CRMChecklist(models.Model):
    _name = 'crm.checklist'
    _description = 'Checklist for the Lead/Opportunity'

    name = fields.Char(string='Name', required=True)
    description = fields.Char(string='Description')
