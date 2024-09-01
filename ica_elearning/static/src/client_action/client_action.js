/** @odoo-module **/

import {registry} from "@web/core/registry";

import {Component,useState,onWillStart} from "@odoo/owl";

class IcaCourseClientAction extends Component {
    setup() {
        this.state = useState({
            courses: []
        })
        this.ormService = this.env.services.orm;
        onWillStart(async () => {
            await this.getAllPublishedCourses();
        })
    }

    async getAllPublishedCourses() {
        this.state.courses = await this.ormService.searchRead('ica.course', [['state', '=', 'published']], ['id', 'name', 'state','fees'], {limit: 5})
    }
}


IcaCourseClientAction.template = "ica_elearning.IcaCourseClientAction";

// remember the tag name we put in the first step
registry.category("actions").add("ica_elearning.IcaCourseClientAction", IcaCourseClientAction);
