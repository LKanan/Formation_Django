from django.contrib import admin
from .models import Products


#  Il est conseillé de créer des classes en les préfixant de Admin puis le nom de la table
class AdminProduct(admin.ModelAdmin):
    # list_display contient les noms des attributs à afficher
    list_display = ("id", "name", "description", "price")


# On doit ajouter la class AdminProduct dans admin.site.register, pour que ses attibuts soients visualisés
admin.site.register(Products, AdminProduct)
