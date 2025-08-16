# Copyright (c) 2025, reagan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Driver(Document):
	def before_save(self):
		pass
#		if self.last_name: #server side script
#			self.full_name = f"{self.first_name} {self.last_name}"
#		else:
#			self.full_name = f"{self.first_name}"
	
	def send_alert(self):
		print("sending alert...")