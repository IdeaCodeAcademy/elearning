/** @odoo-module */

import {registry} from "@web/core/registry"
import {kanbanView} from "@web/views/kanban/kanban_view"
import {KanbanController} from "@web/views/kanban/kanban_controller"
import {useService} from "@web/core/utils/hooks"

const {onWillStart} = owl

class ResPartnerKanbanController extends KanbanController {
    setup() {
        super.setup(...arguments);
        console.log("This is res partner kanban controller")
        this.orm = useService("orm")
        //
        onWillStart(async () => {
            this.customerLocations = await this.orm.readGroup("res.partner", [], ['state_id'], ['state_id'])
        })
    }

    //
    selectLocations(state) {
        this.env.searchModel.splitAndAddDomain(state.__domain)
    }
}

ResPartnerKanbanController.template = "ica_disabled_view.ResPartnerKanbanView"

export const resPartnerKanbanView = {
    ...kanbanView,
    Controller: ResPartnerKanbanController,
}

registry.category("views").add("res_partner_kanban_view", resPartnerKanbanView)