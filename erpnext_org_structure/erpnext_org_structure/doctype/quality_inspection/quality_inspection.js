frappe.ui.form.on("Quality Inspection", {
reference_type:function(frm){
    if(frm.doc.reference_type!="Job Card"){
        frm.set_query("reference_name", function() {
            return {
                filters: {
                    "branch":frm.doc.branch
                }
            };
        });
    }

}
});
