# Formation_Django

## 1. Quelques commandes utiles

- La commande `pip freeze` permet de lister tous les packages python installés dqns lùenvironne,ent virtuel ou global;
  et ceux ci accompagnés de leurs versions.
- On peut rediriger la sortie de cette commande dans un fichier .txt generalement nommé **requirements** en faisant la
  commande `pip freeze > requirements.txt` ce qui permettra à quelqu'un d'autres d'installer les memes dependances pour
  un projet similaire en executant la commande `pip install -r requirements.txt`.
- La methode **dir()** permet de montrer les methode et attibuts d'instance d'une librairie qu'on a importé, par exemple
  on peut visualiser les methodes et attributs d'instance de la librairie pathlib en executant ce
  code:

```
import pathlib

dir(pathlib)
```

Ou encore, on peut visualiser les attibuts et methode d'instance de la classe Path de pathlib en faisant:

```
from pathlib import Path

dir(Path)
```

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
  terminale il faut combiner les touches **Ctrl+c**. Ceci va nous donner le lien qui nous permettra d'acceder à notre
  site dans le navigateur et par defaut c'est *http://127.0.0.1:8000/*, si on entre ce lien dansun navigateur on aura
  une page par defaut de django qui va s'afficher pour nous permettre de nous rendre compte que notre application a bien
  été initialisé.

## 4. Explication de certaines lignes dans le fichier settings.py du projet django

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

## 6. Explication en profondeur de l'architecture minimale d'une application django

L'architecture d'un projet django est en **MVT** contrqirement dans d'autres langage de programmation qui parlent du
**MVC**:

- Le **M** pour dire **Model**, il fait allusion à la base de données et l'architecture de ses tables.
- Le **V** pour dire **View**, généralement il fait allusion à ce qui est visible(le fontend) mais en django le *View*
  se comporte comme le controller.
- Le **C** pour dire **Controler**, il fait allusion à la communication entre les *Views* et *les models*, il joue le
  role du passage intermediaire qui permet l'affichage dans les *Views* des données de la base de donné *models*.  
  En django le **C** est remplacé par **T** pour dire **template**.Et c'est ce *Template* qui prend le role de *View*
  comme dans d'autres architectures.

Une application django est un package qui contient:

- Un dossier **migrations**, c'est un package qui permet d'enregistrer l'architecture de nos tables à et leurs contenus
  dans la base de données à chaque fois qu'on fait des mise à jour d'architecture nos tables(models) comme des dossiers
  pour que ces modifications soient visibles dans l'interface d'administration et cela peut constituer en quelques
  sortes comme un historique des modifications des architectures des tables de notre base de donnnées.
- Le fichier **views.py** est celui qui va contenir nos liens avec la partie *frontend* et chaque lien avec le
  *frontend*
  est une foncton python qui renvoi soit une valeur, soit du JSON.
- Le fichier **models.py** nous permet de créer nos différentes tables pour la base de données, toutes nos tables sont
  sous forme des classes python et doivent héiriter de la classe **Model** qui est un model concu dans django et qui
  contient les nécessaire pour la crétion de nos nouveaux models, cela se fera à l'exemple la syntaxe:

```
from django.db import models

class Custom_model(models.Model):
  ...
```

Par défaut django ajoute un "s" à la fin du nom de chaque table qui est aussi par défaut le nom de la classe pour
designer son pluriel et ce nom est utilisé dans l'interface d'administration, ce qui fait que si on a un nom de table
qui possede déjàun "s" on se retrouve dans l'interface d'administration avec un nom de table avec double "ss", du coup
pour changer ce comportememnt par défaut et définir par nous meme le nom et le pluriel du nom de la table, nous devons
ecrire les meta données(meta data) de la classe de notre table avec une syntaxe ci-dessous dans une sous classe appelée:
**Meta**:

```
from django.db import models

class Custom_model(models.Model):
  class Meta:
    #Pour le nom de la table
    verbose_name="custom_name_table"
    #Pour le pluriel du nom de la table
    verbose_name_plural="custom_plural_name_table"
```

Par défaut les noms de nos objets dans les tables est sous format *nom_Classe(ID)* de l'objet, pour personnaliser ce non
on doit surcharger methode __str__  dans les differentes classes, cette methode nour renvoi la cahine de caractère qui
va représenter le nom de chaque objet de la classe, par exemple pour faire à ce que chaque objet ou enregistrement de 
la table soit reconnu par son nom, on fait:
```
def __str__(self):
    return self.name
```
Il faut savoir qu'on peut prendre n'importe quel attribut ou meme la concateation de ses attributs pour designer le nom 
de l'objet.

Les *champs* d'un model représentent les colonnes de la table et ces champs doivent prendre des types, concernant les
types et leurs arguments obligatoire on doit se referer à la documentation de django en ligne.  
A chaque qu'on vient de modifier quelque chose dans le fichier *models.py* ondoit taper ces deux commandes pour mettre a
jour ces modifications dans la base de données:`python manage.py makemigrations` et `python manage.py migrate`.  
La première commande créera à chqaue fois un fichier python traduit de notre models avec son architecture actuel en le
numérotant; la deuxieme commande viendra comme pour valider les modifications faites dans la base de données.
Pour que nos modifiactions soient visibles dans l'interface d'admninistration on doit traiter cette visualistion dans le
fichiers **admin.py** de notre application

- Le fichier **admin.py** permet de gerer la visualisation de nos tables et leurs champs dans l'interface d'
  administration.
Pour afficher le contenu de la base de données d'une facon minimale ce qui affichera seulement le nom des objets, 
on peut faire:
```
from django.contrib import admin
from .models import Custom_name_class

admin.site.register(Custom_name_class)
```
Mais pour afficher le contenu de la base de données sous forme d'une table en Lignes X Colones on doit augmenter les 
attributs à afficher de cette facon:
```
from django.contrib import admin
from .models import Custom_name_class


class AdminCustom_name_class(admin.ModelAdmin):
    # list_display contient les noms des attributs à afficher, à l'exemple de ca:
    list_display = ("id", "name", "description", "price")

# Ensuite on doit ajouter la classe créée dans admin.site.register
admin.site.register(Custom_name_class, AdminCustom_name_class)
```

L'application centrale qui porte meme le nom du projet a un fichier **urls.py**, ce fichier permet de gerer les routes(
*liens*) de notre site ou projet. chaque *View(Controler)* est caractérisé par un lien qui mène à elle, et c'est grace à
ce lien qu'on peut acceder à un *controler* qui est lui meme dejà associé à une vue(template).


