// Copyright (c) 2025, reagan and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Ride Booking", {
 	refresh(frm) {

 	},
    rate(frm){
        frm.trigger("update_total_amount");
    },

    update_total_amount(frm){

        let total_distance=0;
        let items= frm.doc.items;
        items.forEach((value,key) => {
            total_distance+=value.distance;
            //console.log(`Element at index ${key}: ${value.distance}`);                     
        });
        console.log("total_distance: ",total_distance);
        let amount = total_distance * frm.doc.rate;
        frm.set_value("amount",amount);

    }
 });

frappe.ui.form.on('Ride Booking Item', {
	refresh(frm) {
		// your code here
	},
    distance(frm,cdt,cdn){
        
        /*console.log("cdt: ", cdt);
        console.log("cdn: ", cdn);
        my_child = frappe.get_doc(cdt,cdn);
        console.log("my_child:", my_child);
        frappe.model.set_value(cdt,cdn,"source","updated source");
        console.log("child table distance changed!!");
        */
        frm.trigger("update_total_amount");
    },
    items_remove(frm){
        frm.trigger("update_total_amount");
    }
})
