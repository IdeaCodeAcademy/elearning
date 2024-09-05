/** @odoo-module */

import {standardFieldProps} from "@web/views/fields/standard_field_props";
import {Component, xml} from "@odoo/owl";
import {registry} from "@web/core/registry";

export class MyTextField extends Component {

    /**
     * @param {boolean} newValue
     */
    onChange(newValue) {
        this.props.update(newValue);
    }
}

MyTextField.template = xml`
    <input t-att-id="props.id" class="text-danger" t-att-value="props.value" onChange.bind="onChange" />
`;
MyTextField.props = {
    ...standardFieldProps,
};

MyTextField.supportedTypes = ["char"];
export const myTextField = {
    component: MyTextField
}
registry.category("fields").add("my_text_field", myTextField);
