{
    "name": "Leaflet Map View",
    "description": "Leaflet Map View",
    "version": "1.0",
    "category": "Hidden",
    "installable": True,
    "depends": ["base", "web"],
    "data": ["views/res_partner.xml",],
    "assets": {
        "web.assets_backend": [
            "leaflet_map/static/src/*",
        ]
    },
}
