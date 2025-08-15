import frappe

#@frappe.whitelist(allow_guest=True)//called using postman (http://irfan.cabs:8002/api/v2/method/rentals.rentals.api.get_testapimethod)
@frappe.whitelist()
def get_testapimethod():
    return "testAPImrthodcall"

def throw_message(doc,event):#hook.py -doc_events
    frappe.throw("doc")

def send_payment_remainder_email():
    print("cron schedule job")

def get_query_conditions_for_vehicle(user):
    return "name=1"