from django.shortcuts import render
# HttpResponse nous permet de renvoyer un texte à notre fontend, et ce texte doit etre palcée en lieu de son argument.
from django.http import HttpResponse


# request est un argument obligatoire pour toute vue, pour que ils soient appellable lors des requettes dans le
# navigateur
def home_view(request):
    name = "L-Kanan.dev"
    number = 55
    my_list = [3, 35, 6, 7, 9]
    context = {
        "name": name,
        "number": number,
        "my_list": my_list
    }
    return render(request, "index.html", context)


def contact_view(request):
    return render(request, "products/index.html")


def blog_view(request):
    return HttpResponse("<h1>Blog page</h1>")
