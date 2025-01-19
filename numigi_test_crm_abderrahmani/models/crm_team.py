from odoo import api, fields, models


class CrmTeam(models.Model):
    _inherit = "crm.team"

    team_mails_consolidated = fields.Char("Team mails", compute="_compute_team_mails")

    @api.depends("member_ids")
    def _compute_team_mails(self):
        for team in self:
            team.team_mails_consolidated = " ,".join(
                [member.email for member in team.member_ids]
            )

    @api.model
    def create(self, vals):
        team = super(CrmTeam, self).create(vals)
        if team.user_id and team.user_id not in team.member_ids:
            team.member_ids |= team.user_id
        return team

    def write(self, vals):
        res = super(CrmTeam, self).write(vals)
        if "user_id" in vals:
            if self.user_id not in self.member_ids:
                self.member_ids |= self.user_id
        return res
