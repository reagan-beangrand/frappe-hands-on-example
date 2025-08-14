// Copyright (c) 2025, reagan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
 	refresh(frm) {
        //console.log("refresh");
        if(frm.doc.status ==="New"){

                frm.add_custom_button("Accept", () => {
                    frm.set_value("status","Accepted");
                    frm.save();
                    },"Actions")

                frm.add_custom_button("Reject", () => {
                    frm.set_value("status","Rejected");
                    frm.save();
                    },"Actions")         
        }
 	}
    /*,
    status(frm){
        console.log("status changed!!");
    }
    ,
    onload(frm){
        console.log("onload");
    },
    setup(frm){
        console.log("setup");
    }*/
});
