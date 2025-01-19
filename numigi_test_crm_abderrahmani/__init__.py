# -*- coding: utf-8 -*-
from . import models
from . import tests


def set_default_group_settings(cr, registry):
    from odoo import api, SUPERUSER_ID

    env = api.Environment(cr, SUPERUSER_ID, {})
    default_team_id = env.ref("numigi_test_crm_abderrahmani.crm_team_sales_team")
    # Update de l'utilisation des leads.
    env["ir.config_parameter"].set_param("crm.generate_lead_from_alias", True)
    config = env["res.config.settings"].search([], limit=1, order="id desc")
    if not config:
        config = env["res.config.settings"].create({})
    config.crm_default_team_id = default_team_id.id
    config.group_use_lead = True
    config._compute_generate_lead_from_alias()
    config._compute_crm_alias_prefix()
    config.set_values()
    config.execute()
