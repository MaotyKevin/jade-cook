from django.db import models

class Unite(models.Model):

    MASS = "MASS"
    VOLUME = "VOLUME"
    COUNT = "COUNT"

    UNIT_TYPES = [
        (MASS, "Mass"),
        (VOLUME, "Volume"),
        (COUNT, "Count"),
    ]

    idUnite = models.AutoField(primary_key=True)
    mesure = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)
    unit_type = models.CharField(max_length=10, choices=UNIT_TYPES)

    class Meta:
        db_table = "unite"
        ordering = ["mesure"]
        verbose_name = "Unité"
        verbose_name_plural = "Unités"
    def __str__(self):
        return f"{self.mesure} ({self.abbreviation})"

class Ingredient(models.Model):
    idIngredient = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, unique=True)

    prixUnit = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    stock = models.DecimalField(max_digits=10, decimal_places=3, default=0)

    idUnite = models.ForeignKey(
        "Unite",
        on_delete=models.PROTECT,
        related_name="ingredients"
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ingredient"
        ordering = ["nom"]

    def __str__(self):
        return f"{self.nom} ({self.stock} {self.idUnite.abbreviation})"

class StockMovement(models.Model):

    class MovementType(models.TextChoices):
        PURCHASE = "PURCHASE", "Purchase"
        SALE = "SALE", "Sale"
        LOSS = "LOSS", "Loss"
        ADJUSTMENT = "ADJUSTMENT", "Adjustment"
        PRODUCTION = "PRODUCTION", "Production"

    idMovement = models.AutoField(primary_key=True)

    ingredient = models.ForeignKey(
        "Ingredient",
        on_delete=models.PROTECT,
        related_name="movements"
    )

    movement_type = models.CharField(
        max_length=20,
        choices=MovementType.choices
    )

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=3
    )

    stock_before = models.DecimalField(
        max_digits=10,
        decimal_places=3
    )

    stock_after = models.DecimalField(
        max_digits=10,
        decimal_places=3
    )

    reference_id = models.IntegerField(null=True, blank=True)
    reference_model = models.CharField(max_length=50, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)