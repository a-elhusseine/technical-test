# -*- coding: utf-8 -*-

{
    "name": "Numigi test crm Abderrahmani",
    "version": "1.0",
    "category": "Sales/CRM",
    "summary": "Hello Numigi ",
    "description": """
Module de Test Technique CRM ABDERRAHMANI
=========================================
Ce module permet d'évaluer les compétences techniques du candidat
        """,
    "website": "https://github.com/a-elhusseine",
    "depends": [
        "crm",
        "website_crm",
        "sales_team",
    ],
    "data": [
        "data/crm_team_data.xml",
        "data/ir_cron_data.xml",
        "views/crm_team_views.xml",
        "views/crm_lead_views.xml",
    ],
    "post_init_hook": "set_default_group_settings",
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
}
