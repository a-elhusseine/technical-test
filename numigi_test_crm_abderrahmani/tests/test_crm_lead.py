from odoo.tests.common import TransactionCase

class TestCrmTeam(TransactionCase):
    def setUp(self):
        super(TestCrmTeam, self).setUp()
        # Création d'un utilisateur pour servir de responsable
        self.responsible_user = self.env['res.users'].create({
            'name': 'Responsable Commercial',
            'login': 'responsable@test.com',
            'email': 'responsable@test.com',
        })

        # Création d'un autre utilisateur pour les membres
        self.member_user = self.env['res.users'].create({
            'name': 'Membre Commercial',
            'login': 'membre@test.com',
            'email': 'membre@test.com',
        })

        # Création d'une équipe commerciale
        self.crm_team = self.env['crm.team'].create({
            'name': 'Equipe Commerciale Test',
            'user_id': self.responsible_user.id,  # Responsable de l'équipe
        })

    def test_responsible_in_members(self):
        """Test que le responsable est ajouté automatiquement comme membre de l'équipe"""
        # Vérifier que le responsable est bien membre de l'équipe
        self.assertIn(self.crm_team.user_id, self.crm_team.member_ids,
                      "Le responsable n'est pas comme membre de l'équipe.")

        # Ajouter un autre membre et vérifier
        self.crm_team.member_ids |= self.member_user
        self.assertIn(self.member_user, self.crm_team.member_ids,
                      "Le membre supplémentaire n'a pas été ajouté à l'équipe correctement.")
