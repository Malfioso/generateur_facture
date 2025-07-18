# Invoice Generator

Ce projet est une application Django permettant de gérer des produits et de générer des factures.

## Sommaire

- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Structure du projet](#structure-du-projet)
- [Gestion des médias](#gestion-des-médias)
- [Variables d'environnement](#variables-denvironnement)
- [Commandes utiles](#commandes-utiles)
- [Support](#support)
- [Licence](#licence)

## Prérequis

- Python 3.10 ou supérieur
- pip
- (Recommandé) Outil d'environnement virtuel : `venv`
- Git

## Installation

1. **Cloner le dépôt**

   ```sh
   git clone https://github.com/Malfioso/generateur_facture.git
   cd generateur_facture
   ```

2. **Créer et activer un environnement virtuel**

   ```sh
   python -m venv env
   # Sous Windows :
   env\Scripts\activate
   # Sous macOS/Linux :
   source env/bin/activate
   ```

3. **Installer les dépendances**

   ```sh
   pip install -r requirements.txt
   ```

4. **Appliquer les migrations**

   ```sh
   python invoice/manage.py migrate
   ```

5. **Créer un superutilisateur (accès admin)**

   ```sh
   python invoice/manage.py createsuperuser
   ```

   > Identifiants :
   >
   > - id : gavinj
   > - mot de passe : sxm

6. **Lancer le serveur de développement**

   ```sh
   python invoice/manage.py runserver
   ```

7. **Accéder à l'application**
   - Interface admin : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   - Application principale : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Configuration

- Les paramètres du projet se trouvent dans `invoice/invoice/settings.py`.
- Pour la gestion des fichiers médias (images produits), assurez-vous que le dossier `media/product_images/` existe et est accessible en écriture.
- Pour modifier la base de données, changez la variable `DATABASES` dans `settings.py`.

## Utilisation

- Connectez-vous à l'interface d'administration pour ajouter/modifier des produits et générer des factures.
- Les images des produits doivent être uploadées via l'interface admin ou via les formulaires prévus à cet effet.
- Les factures peuvent être générées et exportées depuis l'application.

## Structure du projet

- `invoice/` : Projet Django principal
  - `manage.py` : Commande de gestion Django
  - `invoice/` : Paramètres et configuration du projet
  - `invoices/` : App pour la gestion des factures
  - `products/` : App pour la gestion des produits
  - `media/` : Dossier pour les fichiers uploadés (images produits)
- `requirements.txt` : Dépendances Python
- `env/` : Environnement virtuel (à ne pas versionner)

## Gestion des médias

- Les images uploadées sont stockées dans `media/product_images/`.
- Pour servir les fichiers médias en développement, Django les gère automatiquement. En production, configurez votre serveur web pour servir ce dossier.

## Variables d'environnement

- Pour la production, pensez à définir la variable `DJANGO_SECRET_KEY` et à configurer `DEBUG=False`.
- Vous pouvez utiliser un fichier `.env` avec [django-environ](https://django-environ.readthedocs.io/) pour gérer vos variables sensibles.

## Commandes utiles

- Créer de nouvelles migrations :
  ```sh
  python invoice/manage.py makemigrations
  ```
- Appliquer les migrations :
  ```sh
  python invoice/manage.py migrate
  ```
- Créer un superutilisateur :
  ```sh
  python invoice/manage.py createsuperuser
  ```
- Démarrer le serveur :
  ```sh
  python invoice/manage.py runserver
  ```

## Support

Pour toute question ou bug, ouvrez une issue sur le [dépôt GitHub](https://github.com/Malfioso/generateur_facture/issues).

## Licence

MIT
