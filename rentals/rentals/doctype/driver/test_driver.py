# Copyright (c) 2025, reagan and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDriver(FrappeTestCase):
	def test_full_name_correctly_set(self):
		test_driver = frappe.new_doc("Driver")
		test_driver.first_name ="testcaseDriver_FN"
		test_driver.last_name ="testcaseDriver_LN"
		test_driver.phone_number ="+911234567890"
		test_driver.license_number = "DL1234"
		test_driver.save()

		self.assertEqual(test_driver.full_name,"testcaseDriver_FN testcaseDriver_LN")

	def test_full_name_correctly_set_when_last_name_isempty(self):
		test_driver = frappe.new_doc("Driver")
		test_driver.first_name ="testcaseDriver_FN"
		#test_driver.last_name ="testcaseDriver_LN"
		test_driver.phone_number ="+911234567890"
		test_driver.license_number = "DL1234"
		test_driver.save()

		self.assertEqual(test_driver.full_name,"testcaseDriver_FN")