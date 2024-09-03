{
    "name": "Disabled View",
    "depends": ["base", "web", "sale_management", "contacts"],
    "data": [
        "views/sale_order.xml",

        "views/res_partner_kanban_view.xml",
    ],
    "assets": {
        "web.assets_backend": {
            "ica_disabled_view/static/src/components/**/*",
            "ica_disabled_view/static/src/res_partner_kanban_view/**/*",
        }
    },
    "license": "LGPL-3"
}
