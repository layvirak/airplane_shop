# Copyright (c) 2024, Lay Virak and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

from datetime import datetime, timedelta

doctype_rent_payment = "Rent Monthly Payment"

class Contract(Document):

	def on_submit(self):
		# change status shop
		# shop_id = self.shop
		# update_shop=frappe.get_doc('Shop',shop_id)
		# update_shop.status="Rented"
		# update_shop.save()

		
		start = datetime.strptime(self.start_date, "%Y-%m-%d")
		end = datetime.strptime(self.date_of_expiry, "%Y-%m-%d")
		result = []
		current_date = start
		while current_date <= end:
			result.append(current_date.strftime("%Y-%m-%d"))
			current_date = current_date.replace(day=1) + timedelta(days=32)
			current_date = current_date.replace(day=1)
			
			doc = frappe.new_doc(doctype_rent_payment)
			doc.contract = self.name
			doc.shop = self.shop
			doc.payment_date = current_date
			doc.rent_amount = self.rent_amount
			doc.tenant = self.tenant
			
			doc.save()
