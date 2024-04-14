from django.shortcuts import render
# HttpResponse nous permet de renvoyer un texte à notre fontend, et ce texte doit etre palcée en lieu de son argument.
from django.http import HttpResponse


# request est un argument obligatoire pour toute vue, pour que ils soient appellable lors des requettes dans le
# navigateur
def home_view(request):
    return HttpResponse("<h1>Hello World</h1>")
