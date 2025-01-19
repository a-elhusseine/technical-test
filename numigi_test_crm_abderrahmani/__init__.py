from . import models


def set_default_group_settings(cr, registry):
    from odoo import api, SUPERUSER_ID

    env = api.Environment(cr, SUPERUSER_ID, {})
    config = env["res.config.settings"].search([], limit=1, order="id desc")
    env["ir.config_parameter"].set_param("crm.generate_lead_from_alias", True)
    config.group_use_lead = True
    config._compute_generate_lead_from_alias()
    config._compute_crm_alias_prefix()
    config.set_values()
