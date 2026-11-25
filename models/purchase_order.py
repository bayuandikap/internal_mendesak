from odoo import models, fields

class PurchaseOrder(models.Model):
	_inherit = 'purchase.order'

	x_catatan_internal = fields.Char(string='Catatan Internal')
	x_mendesak = fields.Boolean(string='Mendesak', default=False)


