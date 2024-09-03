/** @odoo-module */

import {registry} from "@web/core/registry"
import {formView} from "@web/views/form/form_view"
import {FormController} from "@web/views/form/form_controller"
import {useRef, useEffect} from "@odoo/owl";

class SaleOrderFormController extends FormController {
    setup() {
        super.setup(...arguments);
        useEffect(() => {
            //console.log(this.model.root.data.state)
            this.disableForm()
        }, () => [this.model.root.data.state])
        this.onNotebookPageChange = (notebookId, page) =>this.disableForm();
    }

    disableForm() {
        console.log(this.model.root.data.state) // current model of state field
        const inputElements = document.querySelectorAll(".o_form_sheet input")
        const fieldWidgets = document.querySelectorAll(".o_form_sheet .o_field_widget");
        console.log(inputElements);
        if (inputElements) inputElements.forEach(e => e.setAttribute("disabled", 1))
        if (fieldWidgets) fieldWidgets.forEach(e => e.classList.add("pe-none"))
    }
}

const saleOrderFormView = {
    ...formView,
    Controller: SaleOrderFormController,
}

registry.category("views").add("sale_order_form_disable", saleOrderFormView)