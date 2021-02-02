# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Baju(models.Model):
    _name = 'register.baju'
    _description = 'Tabel baju yang ada di database'

    nama = fields.Char()
    ukuran = fields.Selection(selection = [('XL','Extra Large'),
    									   ('L','Large'),
    									   ('M','Medium'),
    									   ('S','Small'),
									      ])
    tipe = fields.Char()
    warna = fields.Char()
    deskripsi = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
