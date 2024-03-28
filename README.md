# Formation_Django

- La commande `pip freeze` permet de lister tous les packages python installés dqns lùenvironne,ent virtuel ou global;
  et ceux ci accompagnés de leurs versions.
- On peut rediriger la sortie de cette commande dans un fichier .txt generalement nommé **requirements** en faisant la
  commande `pip freeze > requirements.txt` ce qui permettra à quelqu'un d'autres d'installer les memes dependances pour
  un projet similaire en executant la commande `pip install -r requirements.txt`.
- Pour créer un projet django on utilise la commande `django-admin startproject nom_du_projet`, ceci créera
  l'architecture minimale d'un projet django avec tous les dossiers et fichiers nécessaires.
- La difference entre un **projet** et une **application** django est que un projet peut contenir plusieurs applications
  django, une application django c'est une facon de subdiviser un projet en petites application qui peuvent etre
  réutilisé dans un autre projet qui nécessite la meme foonctionnalité. 
- Pour créer une application django on utilise la commande `django-admin startapp nom_application`, ceci créera ausi la structure minimale d'une application django.
  Nb: Ne pas oublier de se placer dans le dossier du projet dans le terminal avant la création de l'application.
- 