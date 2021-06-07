# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    std_area = fields.Float(string="STD Area")
    length = fields.Float(string="Length")
    width = fields.Float(string="Width")
    actual_area = fields.Float(string="Actual Area")
    Status = fields.Char(string="Status")
    premium = fields.Float(string="Premium %")
    sold_unsold = fields.Selection([
        ('sold' , 'Sold'),
        ('unsold','Unsold')
    ], default='unsold', string="Sold/Unsold")
    std_rate_per_marla = fields.Float(string="STD Rate Per Marla")
    per_marla_premium = fields.Float(string="Per Marla Premium")
    applicable_rate_per_marla = fields.Float(string="Applicable Rate Per Marla")
    plot_value_per_std_area = fields.Float(string="Plot Value As Per STD Area")
    plot_value_per_actual_area = fields.Float(string="Plot Value As Per Actual Area")
    cash_discount = fields.Float(string="Discount%")
    discount_amount = fields.Float(string="Discount Amount")
    net_amount = fields.Float(string="Net Amount")
    
    
