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

class Vente(models.Model):
    idVente = models.AutoField(primary_key=True)

    date = models.DateTimeField(auto_now_add=True)

    client = models.CharField(max_length=100, null=True, blank=True)

    total = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    montant_recu = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    reste = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

class VentePlat(models.Model):
    idVentePlat = models.AutoField(primary_key=True)

    vente = models.ForeignKey(
        "Vente",
        on_delete=models.CASCADE,
        related_name="items"
    )

    plat = models.ForeignKey(
        "menu.Plat",
        on_delete=models.PROTECT
    )

    qtePlat = models.PositiveIntegerField()

    prix_unitaire = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    total = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )