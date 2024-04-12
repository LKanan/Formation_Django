# Formation_Django

## 1. Quelques commandes utiles

- La commande `pip freeze` permet de lister tous les packages python installés dqns lùenvironne,ent virtuel ou global;
  et ceux ci accompagnés de leurs versions.
- On peut rediriger la sortie de cette commande dans un fichier .txt generalement nommé **requirements** en faisant la
  commande `pip freeze > requirements.txt` ce qui permettra à quelqu'un d'autres d'installer les memes dependances pour
  un projet similaire en executant la commande `pip install -r requirements.txt`.

## 2. Création d'un projet et une application django

- Pour créer un projet django on utilise la commande `django-admin startproject nom_du_projet`, ceci créera
  l'architecture minimale d'un projet django avec tous les dossiers et fichiers nécessaires.
- La difference entre un **projet** et une **application** django est que un projet peut contenir plusieurs applications
  django, une application django c'est une facon de subdiviser un projet en petites application qui peuvent etre
  réutilisé dans un autre projet qui nécessite la meme foonctionnalité.
- Pour créer une application django on utilise la commande `django-admin startapp nom_application`, ceci créera ausi la
  structure minimale d'une application django.  
  **Nb: Ne pas oublier de se placer dans le dossier du projet dans le terminal avant la création de l'application.**

## 3. Lancer le serveur django

- Pour lancer le serveur de django et tester le programme il faut d'abord s'assurer d'etre dans le dossier du projet
  dans le terminal et ensuite taper la commande `python manage.py runserver` et pour arreter le serveur dans le
  terminale il faut combiner les touches **Ctrl+c**.

## 4. Explication de certaines lignes dans le fichier settings du projet

- `BASE_DIR` est une variable qui contient la racine de differnets fichiers de notre projet
- `SECRET_KEY` c'est une variable qui contient une clé secrete du projet et il faut savoir que chaque projet django a sa
  clé secrete et on peut la modifier en inserant d'autre caractere ou en eliminant certains pour la personaliser.
- `DEBUG` c'est une variable booléene qui lorsqu'elle est égale à *True* si notre site renvoi des erreur ces erreurs
  nous seront montrées avec certaines précisions assez technique pour faciliter le debogage c'est pourquoi il recommandé
  de la mettre à *False* lorsqu'on veut deployer le site et là aucune erreur ne sera montrée.
- `ALLOW_HOST` est une variable qui va contenir un nom de domaine pour lequel, s'il est entré dans un navigateur
  celui-ci permettra aussi de lance notre site.
- `INSTALLED_APPS` c'est une variable qui contient toutes les application créées dans notre projet, et donc à chqaue
  fois aue nous créons un projet on doit venir ajouter son nom sur cette liste pour qu'elle soit reconnu sinon au cas où
  on tenterait de l'utiliser sans l'avoir ajouter à la liste dans les settings, cela va nous genenerer des erreurs.
- `MIDDLEWARE` c'est une variable qui contient une liste d'élements pour la securité et l'authentification.
- `ROOT_URLCONFIG` c'est une variable qui contient le chemin ou la localisation du fichier dans lequel nos root ou nos
  urls seront stockés.

[//]: # (TODO: Il faut expliquer  ce point lorsque je vais y arriver)

- `TEMPLATES`
- `WSGI_APPLICATION` on dirait qui représente notre serveur local.
- `DATABASE` c'est une variable qui contient la spécification de la *SGBD* que l'on va utiliser pour notre projet et par
  defaut django nous permet d'utiliser *SQL* et specifie le chemin de la base de données utilisée, exemple par defaut on
  a : `'NAME': BASE_DIR/ 'db.sqlite3'` puisque *BASE_DIRE* represente la racine qui est notre projet alors on pointe
  vers le fichier *db.sqlite3* si on change cette valeur et qu'on relance le serveur on verra que le nouveau nom sera
  ajouter comme fichier à la racine de notre projet s'il n'existe pas encore.
- `AUTH_PASSWORD_VALIDATORS` c'est une variable qui contient la liste des differentes erreurs qui peuvent etre levées
  lors de la monipulation des mots de passe
- `LANGUAGE_CODE` c'est une variable qui contient la langue par defaut de notre site, on peut changer sa valeur, par
  exemple lorsque on leve des erreur de mot de passe si la valeur est à l'anglais l'erreur sera levé en anglais mais si
  c'est en francais le message sera en francais et meme l'interface d'administration prend la langue définie, si on
  change la langue ici, meme dans l'interface d'administration tout sera configurer dans cette langue là.
- `TIME_ZONE` est aussi une variable pour signifier le fuseau horaire utilisé par notre site
- `STATIC_URL` c'est une variable qui permet de signifier que tous les fichiers static(ex: les fichiers css, js et les
  images) seront dans le dossier parent au nom de `static/`, ce qui fera que lorsque dans un fichier on veut mettre un
  chemin vers un fichier static on aura meme pas besoi d'ecrire le chemin en commencant par le mot static on aura qu'a
  commencé par le fichier ou le dossier qui vient directement dans le dossier static.

[//]: # (TODO: Il faut expliquer  ce point lorsque je vais y arriver)

- `DEFAULT_AUTO_FIELD`

## 5. Fonctionnement du localhost et du superuser

- **Le localhost**  
  Quand on lance le serveur django il lance notre application à l'adresse *http://127.0.0.1:8000/*; **http://127.0.0.1:
  **
  represente l'adresse local de toute machine et **8000/** est le port par defaut sur lequel notre application est
  lancée mais on peut personnaliser le port sur lequel notre application sera lancée en executant la
  commande `python manage.py runserver custom_port`, ex: `python manage.py runserver 8070` cette commande lancera notre
  application sur le port 8070 et notre site sera accessible à l'adresse *http://127.0.0.1:8070/*. Ceci peut nous etre
  utile lorsque on a lancé plusieurs application au meme moment et ainsi on poura evite des conflits des ports, pour
  cahque application son port.
- **Le superuser**  
  La commande `python manage.py migrate` permet de mettre à jour les modifications effectuées sur la structure des
  tables(models) de la base de données et chaque fois qu'on effectue les migrations le dossier créé enregistre l'etat de
  la base de données avec son contenu, on peut effacer les nouvelles migrations pour rentrer à un état anterieur de la
  base de données, si ces mise à jour ne sont pas faits, les modifications de la structure des tables ne seronts pas
  pris en compte.  
  Avant le lancement du serveur surtout pour la première fois, il est conseillé d'executer cette commande.
  Le **supersuser** est considerer comme l'administrateur du site web c'est un utilisateur qui a accès à l'interface d'
  administretion.
  Pour créer un superuser ou l'utilisateur administrateur on execute la commande `python manage.py createsuperuser` puis
  on suit les etapes pour définir le nom, l'adresse e-mail et le mot de passe. et il n'y a que ce superuser qui peut
  acceder à l'interface d'administration au lien http://127.0.0.1:8000/admin.