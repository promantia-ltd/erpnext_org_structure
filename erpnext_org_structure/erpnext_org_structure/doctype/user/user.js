frappe.ui.form.on('User', {
refresh:function(frm){
}
})

frappe.ui.form.on('Branch Details', {
branch:function(frm,cdt,cdn){
    var branch=frm.doc.branch_details;
     for(var i=0; i< branch.length; i++) {
	for(var j=i+1; j<branch.length; j++) {
   		if(branch[i].branch===branch[j].branch) {
             frappe.throw(__(" Same Branch  '"+branch[j].branch+"' cannot be added twice."));
         }
     }
     }
},
before_branch_details_remove:function(frm,cdt,cdn) {
    var row=frappe.get_doc(cdt,cdn);
    console.log(row)
    frappe.call({
        method:"erpnext_org_structure.erpnext_org_structure.doctype.user.user.delete_user_permission",
        args:{
        user:frm.doc.email,
        branch:row.branch	
    },
        async:false,
        callback: function(r){
    }
    });
}
})
