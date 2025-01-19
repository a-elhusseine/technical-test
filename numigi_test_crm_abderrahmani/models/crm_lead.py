from datetime import timedelta
from odoo import models, fields, api
from werkzeug.urls import url_join


class CrmLead(models.Model):
    _inherit = "crm.lead"

    def _notify_team_if_stagnant(self):
        stagnant_leads = self.search(
            [
                (
                    "stage_id",
                    "=",
                    self.env.ref("crm.stage_lead1").id,
                ),  # Assuming "draft" stage
                ("create_date", "<", fields.Datetime.now() - timedelta(days=10)),
            ]
        )

        for lead in stagnant_leads:
            team = lead.team_id
            if team and team.team_mails_consolidated:
                # Choix du mail car il s'agit d'un besoin deja exprimé dont son utilité est possible .
                email_addresses = team.team_mails_consolidated
                subject = f"Attention: Opportunité stagnante - {lead.name}"
                web_base_url = self.env["ir.config_parameter"].get_param("web.base.url")
                lead_url = url_join(
                    web_base_url, f"/web#id={self.id}&model=crm.lead&view_type=form"
                )
                body = f"""
                    <p>Bonjour,</p>
                    <p>Merci de donner une suite à cette opportunité <a href="{lead_url}">{lead.name}</a>.</p>
                    <p>Cordialement.</p>
                """
                # Créer et envoyer l'e-mail
                mail = self.env["mail.mail"].create(
                    {
                        "subject": subject,
                        "body_html": body,
                        "email_to": email_addresses,
                        "author_id": self.env.user.partner_id.id,
                    }
                )
                mail.send()
