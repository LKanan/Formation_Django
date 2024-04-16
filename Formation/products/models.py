from django.db import models


# Toute classe(model) doit hériter de la classe Model de models
class Products(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    # Pour le DecimalField on a deux arguments obligatoires, max digit qui représente le nombre maximum des chiffres que
    # peut avoir ce nombre decimal et le decimal_place représente lenombre des chiffres après la virgule.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Le type image en django nécessite l'installation de la librairie pillow pour traiter les images
    image = models.ImageField(upload_to="images", blank=True)
    image2 = models.ImageField(upload_to="images2", null=True )
    actif = models.BooleanField(default=True)

    # La classe Meta est une sous-classe pour modifier les meta data de la classe, genre ses proprietés.
    class Meta:
        # verbose_name est la variable qui contient le nom de mon model ou ma teble, et c'est ce nom quii sera utilisé
        # dans l'interface d'administration pour desingner ma table
        verbose_name = "Product"
        # verbose_name_plural est la variable qui va contenir la chaine de caractèes qui va designer le pluriel du nom
        # de ma table et c'est le nom qui sera aussi utilisé dans l'interface d'administration
        verbose_name_plural = "Products"

    # La methode __str__ est une methode de classe que nous allons surcharger pour définir le nom de nos objets dans la
    # table
    def __str__(self):
        return self.name
