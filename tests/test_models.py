from odoo.tests import common, tagged


@tagged('at_install', 'post_install')
class TestModel(common.TransactionCase):

	def setUp(self):
		super(TestModel, self).setUp()
		self.test_obj = self.env['register.baju'].sudo()

	def test_model_exists(self):
		self.assertTrue(self.test_obj._name, 'register.baju')

	def test_model_valid_data(self):
		baju = self.test_obj.create({
    		'nama' : 'Baju X',
    		'ukuran' : 'XL',
    		'tipe' : 'tipe X',
    		'warna' : 'warna X',
    		'deskripsi' : 'deskripsi X'
    	})
		self.assertTrue(bool(self.test_obj.search([('id', '=', baju.id)], limit=1)))

