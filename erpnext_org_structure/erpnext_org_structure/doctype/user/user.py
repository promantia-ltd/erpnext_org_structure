# -*- coding: utf-8 -*-
# Copyright (c) 2020, seabridge_app and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class User(Document):
	pass

def on_save(self,document):
	for row in self.branch_details:
		if not frappe.db.exists("User Permission",{'user':self.email,'allow':'Branch','for_value':row.branch}):           
			up_doc=frappe.get_doc(dict(doctype = 'User Permission',
				            user=self.email,
				            allow="Branch",
				            for_value=row.branch,
				            apply_to_all_doctypes=1
				)).insert(ignore_mandatory=True)
			up_doc.save()

@frappe.whitelist()
def delete_user_permission(user,branch):
	name=frappe.db.get_value("User Permission",{'user':user,'allow':'Branch','for_value':branch},'name')
	if name:
		frappe.delete_doc("User Permission",name)