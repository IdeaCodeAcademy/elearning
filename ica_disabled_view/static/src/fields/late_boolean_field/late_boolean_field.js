/** @odoo-module */

import {registry} from "@web/core/registry";
import {booleanField, BooleanField} from "@web/views/fields/boolean/boolean_field";

export class LateOrderBooleanField extends BooleanField {
    setup() {
        super.setup();
        console.log("hello from existing widget inherit")
    }
}

export const lateOrderBooleanField = {
    ...booleanField,
    component: LateOrderBooleanField
}
LateOrderBooleanField.template = "ica_disabled_view.LateOrderBooleanField";
registry.category("fields").add("late_boolean", lateOrderBooleanField);
