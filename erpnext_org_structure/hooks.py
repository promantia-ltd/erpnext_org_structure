# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

import erpnext.accounts.general_ledger as _standard_gl
import erpnext_org_structure.api as _custom_api

app_name = "erpnext_org_structure"
app_title = "erpnext_org_structure"
app_publisher = "admin"
app_description = "erpnext_org_structure"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "admin@gmail.com"
app_license = "MIT"

_standard_gl.validate_accounting_period = _custom_api.validate_accounting_period

accounting_dimension_doctypes = ["GL Entry", "Sales Invoice", "Purchase Invoice", "Payment Entry", "Asset",
	"Expense Claim", "Expense Claim Detail", "Expense Taxes and Charges", "Stock Entry", "Budget", "Payroll Entry", "Delivery Note",
	"Sales Invoice Item", "Purchase Invoice Item", "Purchase Order Item", "Journal Entry Account", "Material Request Item", "Delivery Note Item",
	"Purchase Receipt Item", "Stock Entry Detail", "Payment Entry Deduction", "Sales Taxes and Charges", "Purchase Taxes and Charges", "Shipping Rule",
	"Landed Cost Item", "Asset Value Adjustment", "Loyalty Program", "Fee Schedule", "Fee Structure", "Stock Reconciliation",
	"Travel Request", "Fees", "POS Profile", "Opening Invoice Creation Tool", "Opening Invoice Creation Tool Item", "Subscription",
	"Subscription Plan"
]

fixtures = [
{"dt": "Custom Field",
		"filters": [
         [
	 "name", "in", [
		"User-branch_details_section",
		"User-branch_details",
		"Branch-address",
		"Branch-abbr"
	]
	]
]
}
]

doctype_js = {
	"User" : "erpnext_org_structure/doctype/user/user.js",
	"Quality Inspection" : "erpnext_org_structure/doctype/quality_inspection/quality_inspection.js",
	"Branch" : "erpnext_org_structure/doctype/branch/branch.js"
}
doc_events = {
    	"User": {
		"after_insert": ["erpnext_org_structure.erpnext_org_structure.doctype.user.user.on_save"],
		"on_update":["erpnext_org_structure.erpnext_org_structure.doctype.user.user.on_save"]
}
}

override_doctype_class = {
	'Accounting Period': 'erpnext_org_structure.api.CustomAccountingPeriod'
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_org_structure/css/erpnext_org_structure.css"
# app_include_js = "/assets/erpnext_org_structure/js/erpnext_org_structure.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_org_structure/css/erpnext_org_structure.css"
# web_include_js = "/assets/erpnext_org_structure/js/erpnext_org_structure.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "erpnext_org_structure/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_org_structure.install.before_install"
# after_install = "erpnext_org_structure.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_org_structure.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_org_structure.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_org_structure.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_org_structure.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_org_structure.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_org_structure.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_org_structure.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_org_structure.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "erpnext_org_structure.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"erpnext_org_structure.auth.validate"
# ]

