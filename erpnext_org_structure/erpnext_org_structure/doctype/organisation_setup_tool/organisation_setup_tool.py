# -*- coding: utf-8 -*-
# Copyright (c) 2021, admin and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import scrub
from frappe.utils import cstr
from frappe.custom.doctype.custom_field.custom_field import create_custom_field


class OrganisationSetupTool(Document):
    def validate(self):
        exists = frappe.db.get_value("Organisation Setup Tool", {
                                     'reference_document_type': self.reference_document_type}, ['name'])

        if exists and self.is_new():
            frappe.throw("Reference Document Type already exists")

        if not self.is_new():
            self.validate_document_type_change()

        make_dimension_in_accounting_doctypes(doc=self)

    def validate_document_type_change(self):
        doctype_before_save = frappe.db.get_value(
            "Organisation Setup Tool", self.name, "reference_document_type")
        if doctype_before_save != self.reference_document_type:
            message = _("Cannot change Reference Document Type.")
            message += _("Please create a new Accounting Dimension if required.")
            frappe.throw(message)

    def on_trash(self):
        delete_accounting_dimension(doc=self)


def make_dimension_in_accounting_doctypes(doc):
    doclist = get_doctypes_with_dimensions()

    for val in doc.injected_document_details:
        if val.reference_document not in doclist:
            df = {
                "fieldname": doc.fieldname,
                "label": doc.label,
                "fieldtype": "Link",
                "options": doc.reference_document_type,
                "insert_after": 'company',
                "owner": "Administrator"
            }

            meta = frappe.get_meta(val.reference_document, cached=False)
            link_doctypes = [d.options for d in meta.get("fields")]

            if df['options'] not in link_doctypes:
                create_custom_field(val.reference_document, df)

            frappe.clear_cache(doctype=val.reference_document)

        else:
            frappe.throw(_("Unable to add the {0} as the {1} is available in {2} as accounting dimension.").format(
                doc.label, doc.reference_document_type, val.reference_document))


def get_doctypes_with_dimensions():
    return frappe.get_hooks("accounting_dimension_doctypes")


def delete_accounting_dimension(doc):
    for val in doc.injected_document_details:
        frappe.db.sql("""delete from `tabCustom Field` where fieldname = %s AND dt = %s""",
                      (doc.label, val.reference_document))


@frappe.whitelist()
def delete_custom_field(doc, doctype):
    frappe.db.sql("""delete from `tabCustom Field` where fieldname = %s AND dt = %s""",
                  (doc, doctype))
