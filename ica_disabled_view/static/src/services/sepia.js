/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component,useService } from "@odoo/owl";

class SepiaEffect extends Component {}
SepiaEffect.template = 'ica_disabled_view.SepiaEffect';

export function sepiaEffectProvider(env, params = {}) {
    return {
        Component: SepiaEffect,
    };
}

const effectRegistry = registry.category("effects");
effectRegistry.add("sepia", sepiaEffectProvider);

// const effectService = useService("effect");
// effectService.add({ type: "sepia" });