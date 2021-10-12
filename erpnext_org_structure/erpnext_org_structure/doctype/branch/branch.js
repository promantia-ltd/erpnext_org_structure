frappe.ui.form.on('Branch', {
	refresh(frm) {
		frm.set_query("address", function() {
            return {
                filters: {
                    "is_your_company_address":1
                }
            };
        });
	}
});
