# -*- coding: utf-8 -*-
from odoo import http
import json

class RegisterBaju(http.Controller):
    @http.route('/register_baju/', auth='public', methods=['GET'])
    def index(self, **kw):
        Baju = http.request.env['register.baju'].sudo().search_read([])
        return http.Response(json.dumps(Baju, default=str), status=200, content_type="application/json")

    @http.route('/register_baju/add', auth='public', methods=['POST'], csrf=False)
    def posts(self, **kw):
    	try:
    		nama = kw.get('nama')
    		ukuran = kw.get('ukuran')
    		tipe = kw.get('tipe')
    		warna = kw.get('warna')
    		deskripsi = kw.get('deskripsi')

    		temp = {
    			'nama' : nama,
    			'ukuran' : ukuran,
    			'tipe' : tipe,
    			'warna' : warna,
    			'deskripsi' : deskripsi
    		}
    		http.request.env['register.baju'].sudo().create(temp)

    		return http.Response("Success",status=200, content_type="application/json")

    	except:

    		return http.Response(json.dumps({"error":"error"}))

#     @http.route('/register_baju/register_baju/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('register_baju.listing', {
#             'root': '/register_baju/register_baju',
#             'objects': http.request.env['register_baju.register_baju'].search([]),
#         })

#     @http.route('/register_baju/register_baju/objects/<model("register_baju.register_baju"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('register_baju.object', {
#             'object': obj
#         })
