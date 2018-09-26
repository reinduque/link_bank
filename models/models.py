# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Link(models.Model):
    _name = 'link_bank.link'
    _inherit = ['mail.thread']

    _rec_name = 'name'

    name = fields.Char(
        string='Title',
        required=True,
    )

    url = fields.Char(
        string='URL',
        required=True,
    )

    username = fields.Char(
        string='Username',
    )

    password = fields.Char(
        string='Password',
    )

    notes = fields.Text(
        string='Description',
    )

    category_id = fields.Many2one(
        'link_bank.category',
        string='Category',
    )

    tag_ids = fields.Many2many(
        'link_bank.tags',
        string='Tags',
    )

class LinkCategory(models.Model):
    _name = 'link_bank.category'

    name = fields.Char(
        string='Category Name',
    )

class LinkTags(models.Model):
    _name = 'link_bank.tags'
    
    name = fields.Char(
        string='Tag',
        required=True,
    )
# class link_bank(models.Model):
#     _name = 'link_bank.link_bank'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100