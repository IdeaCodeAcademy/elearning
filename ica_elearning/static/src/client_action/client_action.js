/** @odoo-module **/

import { registry } from "@web/core/registry";

import { Component } from  "@odoo/owl";

class IcaCourseClientAction extends Component {}
IcaCourseClientAction.template = "ica_elearning.IcaCourseClientAction";

// remember the tag name we put in the first step
registry.category("actions").add("ica_elearning.IcaCourseClientAction", IcaCourseClientAction);
