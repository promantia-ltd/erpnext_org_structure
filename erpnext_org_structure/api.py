import frappe
from frappe import _
from erpnext.accounts.doctype.accounting_period.accounting_period import AccountingPeriod
class OverlapError(frappe.ValidationError): pass
class ClosedAccountingPeriod(frappe.ValidationError): pass

class CustomAccountingPeriod(AccountingPeriod):
	def validate_overlap(self):    
		branch_field = frappe.db.get_value("Injected Document Details",{"reference_document":"Accounting Period","parent":"Branch","parenttype":"Organisation Setup Tool"},"reference_document")
		if branch_field:
			existing_accounting_period = frappe.db.sql("""select name from `tabAccounting Period`
				where (
				(%(start_date)s between start_date and end_date)
				or (%(end_date)s between start_date and end_date)
				or (start_date between %(start_date)s and %(end_date)s)
				or (end_date between %(start_date)s and %(end_date)s)
				) and name!=%(name)s and company=%(company)s and branch=%(branch)s""",
				{
				"start_date": self.start_date,
				"end_date": self.end_date,
				"name": self.name,
				"company": self.company,
				"branch":self.branch
				}, as_dict=True)

			if len(existing_accounting_period) > 0:
				frappe.throw(_("Accounting Period overlaps with {0}").format(existing_accounting_period[0].get("name")), OverlapError)
		else:
			existing_accounting_period = frappe.db.sql("""select name from `tabAccounting Period`
				where (
				(%(start_date)s between start_date and end_date)
				or (%(end_date)s between start_date and end_date)
				or (start_date between %(start_date)s and %(end_date)s)
				or (end_date between %(start_date)s and %(end_date)s)
				) and name!=%(name)s and company=%(company)s""",
				{
				"start_date": self.start_date,
				"end_date": self.end_date,
				"name": self.name,
				"company": self.company
				}, as_dict=True)

			if len(existing_accounting_period) > 0:
				frappe.throw(_("Accounting Period overlaps with {0}").format(existing_accounting_period[0].get("name")), OverlapError)

def validate_accounting_period(gl_map):
	AD = frappe.db.get_value("Accounting Dimension",{"document_type":"Branch"},"document_type")
	branch_field = frappe.db.get_value("Injected Document Details",{"reference_document":"Accounting Period","parent":"Branch","parenttype":"Organisation Setup Tool"},"reference_document")
	if branch_field and AD:
		accounting_periods = frappe.db.sql(""" SELECT
				ap.name as name
			FROM
				`tabAccounting Period` ap, `tabClosed Document` cd
			WHERE
				ap.name = cd.parent
				AND ap.company = %(company)s
				AND cd.closed = 1
				AND cd.document_type = %(voucher_type)s
				AND %(date)s between ap.start_date and ap.end_date
				AND ap.branch = %(branch)s
				""", {
					'date': gl_map[0].posting_date,
					'company': gl_map[0].company,
					'voucher_type': gl_map[0].voucher_type,
					'branch': gl_map[0].branch
				}, as_dict=1)

		if accounting_periods:
			frappe.throw(_("You cannot create or cancel any accounting entries with in the closed Accounting Period {0}")
				.format(frappe.bold(accounting_periods[0].name)), ClosedAccountingPeriod)
	
	else:
		accounting_periods = frappe.db.sql(""" SELECT
				ap.name as name
			FROM
				`tabAccounting Period` ap, `tabClosed Document` cd
			WHERE
				ap.name = cd.parent
				AND ap.company = %(company)s
				AND cd.closed = 1
				AND cd.document_type = %(voucher_type)s
				AND %(date)s between ap.start_date and ap.end_date
				""", {
					'date': gl_map[0].posting_date,
					'company': gl_map[0].company,
					'voucher_type': gl_map[0].voucher_type
				}, as_dict=1)

		if accounting_periods:
			frappe.throw(_("You cannot create or cancel any accounting entries with in the closed Accounting Period {0}")
				.format(frappe.bold(accounting_periods[0].name)), ClosedAccountingPeriod)
