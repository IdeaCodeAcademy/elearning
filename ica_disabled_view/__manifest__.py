{
    "name": "Disabled View",
    "depends": ["base","web","sale_management"],
    "data": [
        "views/sale_order.xml",
    ],
    "assets": {
        "web.assets_backend": {
            "ica_disabled_view/static/src/components/**/*"
        }
    },
    "license": "LGPL-3"
}
