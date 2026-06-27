from django.db import models

class Plat(models.Model):
    idPlat = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, unique=True)
    prixVente = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom

class PlatIngredient(models.Model):
    id = models.AutoField(primary_key=True)

    plat = models.ForeignKey("Plat", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("Ingredient", on_delete=models.PROTECT)

    quantity = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        db_table = "plat_ingredient"
        unique_together = ("plat", "ingredient")
