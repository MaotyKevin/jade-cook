from django.db import models

class Achat(models.Model):
    idAchat = models.AutoField(primary_key=True)

    date = models.DateTimeField(auto_now_add=True)

    total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    fournisseur = models.CharField(max_length=100, null=True, blank=True)

class AchatIngredient(models.Model):
    idAchatIngredient = models.AutoField(primary_key=True)

    achat = models.ForeignKey(
        "Achat",
        on_delete=models.CASCADE,
        related_name="items"
    )

    ingredient = models.ForeignKey(
        "inventory.Ingredient",
        on_delete=models.PROTECT
    )

    qteAcheté = models.DecimalField(
        max_digits=10,
        decimal_places=3
    )

    prixUnitaire = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    total = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
