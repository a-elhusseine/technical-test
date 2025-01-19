
# Module : `numigi_test_crm_abderrahmani`

Ce module répond à une série de personnalisations pour le module CRM dans Odoo 14 (Community et Enterprise). Il est conçu pour répondre aux spécifications fonctionnelles détaillées sur le test .

## Fonctionnalités principales

### 1. **Ajout d'un champ "Emails" sur l'équipe commerciale**
   - Un champ "team_mails_consolidated" est ajouté au modèle des équipes commerciales (`crm.team`).
   - Ce champ contient tous les emails des membres de l'équipe, séparés par des virgules, et est mis à jour automatiquement.

### 2. **Chef d'équipe comme membre de l'équipe commerciale**
   - Lorsqu'un chef d'équipe est désigné, il est automatiquement ajouté à la liste des membres de l'équipe commerciale correspondante s'il n'y figure pas déjà.
   - Ceci passe par create et write pour interagir efficacement .

### 3. **Création d'équipes commerciales par défaut**
   - À l'installation du module, trois équipes commerciales sont créées via un fichier de données :
     1. **Équipe Support Technique**
     2. **Équipe Ventes**
     3. **Équipe SAV**
   -Ceux ci sont present sur le repertoire numigi_test_crm_abderrahmani/data/crm_team_data.xml .

### 4. **Paramètres de configuration CRM activés par défaut**
   - Les paramètres mentionnés (activation des leads ...) se font par le bais d'un `post_init_hook` present dans le premier fichier `__init__.py` sous le nom de `set_default_group_settings` .

### 5. **Notification pour les opportunités inactives**
   - Un cron s'execute quotidiennement ,Si une opportunité reste au statut "draft" plus de 10 jours après sa création, une notification est envoyée à tous les membres de l'équipe commerciale associée.
   - Le nom de l'opportunité est un lien redirigeant vers son formulaire.

### 6. **Restriction du champ "Revenu espéré"**
   - Le champ "Revenu espéré" est visible uniquement pour les utilisateurs appartenant au groupe "Administrateur des Ventes".
   - le champs est present dans beacoup de vues , potail et qweb et les variables ne sont pas protegé , ce qui rends l'utilisation de la propriété `group=` dans le champs aura enormement d'effet de bord .   
   - Heritage directement de la vue et ajouter la contrainte de groupe . (PS Le champs reste tout de meme accessible meme si non affiché) et cela s'applique aux vues :
     - Kanban
     - Formulaire
     - Liste

### 7. **Assignation automatique à l'équipe "Équipe Ventes"**
   - Lorsqu'une piste est créée via le formulaire de contact disponible sur le site web (module `website_crm`), elle est automatiquement assignée à l'équipe "Équipe Ventes".