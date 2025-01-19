# Module : `numigi_test_crm_abderrahmani`

Ce module répond à une série de personnalisations pour le module CRM dans Odoo 14 (Community et Enterprise). Il est conçu pour répondre aux spécifications fonctionnelles détaillées sur le test.

## Fonctionnalités principales

### 1. **Ajout d'un champ "Emails" sur l'équipe commerciale**

- Un champ "team\_mails\_consolidated" est ajouté au modèle des équipes commerciales (`crm.team`).
- Ce champ contient tous les emails des membres de l'équipe, séparés par des virgules, et est mis à jour automatiquement.

### 2. **Chef d'équipe comme membre de l'équipe commerciale**

- Lorsqu'un chef d'équipe est désigné, il est automatiquement ajouté à la liste des membres de l'équipe commerciale correspondante s'il n'y figure pas déjà.
- Ceci passe par les méthodes `create` et `write` pour interagir efficacement.

### 3. **Création d'équipes commerciales par défaut**

- À l'installation du module, trois équipes commerciales sont créées via un fichier de données :
  1. **Équipe Support Technique**
  2. **Équipe Ventes**
  3. **Équipe SAV**
- Ceux-ci sont présents dans le répertoire `numigi_test_crm_abderrahmani/data/crm_team_data.xml`.

### 4. **Paramètres de configuration CRM activés par défaut**

- Les paramètres mentionnés (activation des leads, etc.) se font par le biais d'un `post_init_hook` présent dans le fichier `__init__.py` sous le nom de `set_default_group_settings`.

### 5. **Notification pour les opportunités inactives**

- Un cron s'exécute quotidiennement. Si une opportunité reste au statut "Draft" plus de 10 jours après sa création, une notification est envoyée à tous les membres de l'équipe commerciale associée.
- Le nom de l'opportunité est un lien redirigeant vers son formulaire.

### 6. **Restriction du champ "Revenu espéré"**

- Le champ "Revenu espéré" est visible uniquement pour les utilisateurs appartenant au groupe "Administrateur des Ventes".
- Le champ est présent dans plusieurs vues (portail et QWeb) et les variables ne sont pas protégées, ce qui rend l'utilisation de la propriété `groups=` dans le champ problématique. Cela pourrait causer des effets de bord.
- Solution : hériter directement de la vue et ajouter la contrainte de groupe. (PS : le champ reste tout de même accessible même si non affiché). Cette restriction s'applique aux vues suivantes :
  - Kanban
  - Formulaire
  - Liste

### 7. **Assignation automatique à l'équipe "Équipe Ventes"**

- Lorsqu'une piste est créée via le formulaire de contact disponible sur le site web (module `website_crm`), elle est automatiquement assignée à l'équipe "Équipe Ventes".

---

## Points de vigilance


- **Restriction du champ "Revenu espéré"** :

  - Bien que le champ soit restreint dans les vues, il reste accessible via des appels techniques ou API .

---

## Tests CRM Leads
### 1. **Tests unitaires :**
  - Vérification de l'ajout automatique du chef d'équipe dans les membres de l'équipe lors de la création ou modification (`-i numigi_test_crm_abderrahmani --test-enable --log-level=test`).

### 2. **Tests d'intégration :**

- Création d'une piste via le formulaire de contact du site web et vérification de l'assignation automatique à l'équipe "Équipe Ventes".
- Simulation d'une opportunité inactive pendant 10 jours et vérification de l'envoi des notifications.

### 3. **Tests d'accès et permissions :**

- Vérification que le champ "Revenu espéré" n'est visible que pour les administrateurs des ventes.
