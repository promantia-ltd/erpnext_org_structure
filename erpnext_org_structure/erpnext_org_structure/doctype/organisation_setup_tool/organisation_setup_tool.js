// Copyright (c) 2021, admin and contributors
// For license information, please see license.txt

frappe.ui.form.on("Organisation Setup Tool", {
	refresh: function (frm) {
		var reference_document = ["Branch", "Department", "Territory"]
		frm.set_query("reference_document_type", function () {
			return {
				filters: {
					"name": ["in", reference_document]
				}
			};
		});
		frm.fields_dict['injected_document_details'].grid.get_field('reference_document').get_query = function () {
			return {
				filters: {
					"istable": 0
				}
			}
		}

	},
	label: function (frm) {
		frm.set_value('fieldname', frappe.model.scrub(frm.doc.reference_document_type));
	}

});

frappe.ui.form.on("Injected Document Details", {
	before_injected_document_details_remove: function (frm, cdt, cdn) {
		var row = frappe.get_doc(cdt, cdn);
		frappe.call({
			method: "erpnext_org_structure.erpnext_org_structure.doctype.organisation_setup_tool.organisation_setup_tool.delete_custom_field",
			args: {
				doc: frm.doc.name,
				doctype: row.reference_document
			},
			async: false,
			callback: function (r) {
			}
		});
	}
})
