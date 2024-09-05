{
    "name": "Disabled View",
    "depends": ["base", "web", "sale_management", "leaflet_map"],
    "data": [
        "views/sale_order.xml",

        "views/res_partner_kanban_view.xml",
        "views/res_partner_widget.xml",
    ],
    "assets": {
        "web.assets_backend": {
            "ica_disabled_view/static/src/**/*",
            # "/ica_disabled_view/static/src/res_partner_kanban_view/**/*",
            # "/ica_disabled_view/static/src/username_field/**/*",
            # "/ica_disabled_view/static/src/mytext_field/**/*",
            # "/ica_disabled_view/static/src/date_picker/**/*",
        }
    },
    "license": "LGPL-3"
}
