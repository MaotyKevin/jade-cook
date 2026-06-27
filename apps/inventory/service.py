# inventory/services.py

from decimal import Decimal
from django.db import transaction

from inventory.models import Ingredient, StockMovement
from menu.models import Plat


@transaction.atomic
def process_achat(achat):
    total_achat = Decimal("0")

    for item in achat.items.all():
        ingredient = item.ingredient

        qty = Decimal(item.qteAcheté)
        price = Decimal(item.prixUnitaire)

        line_total = qty * price
        item.total = line_total
        item.save()

        total_achat += line_total

        # stock update
        before = ingredient.stock
        after = before + qty

        ingredient.stock = after
        ingredient.prixUnit = price  # optional update (last price)
        ingredient.save()

        # stock movement
        StockMovement.objects.create(
            ingredient=ingredient,
            movement_type="PURCHASE",
            quantity=qty,
            stock_before=before,
            stock_after=after,
            reference_id=achat.idAchat,
            reference_model="Achat"
        )

    achat.total = total_achat
    achat.save()


@transaction.atomic
def deduct_stock_for_sale(plat: Plat, quantity: int, vente_id=None):
    """
    Deduct ingredients based on recipe when a dish is sold.
    """

    # Get all recipe ingredients
    recipe_items = plat.recettes.all()

    for item in recipe_items:
        ingredient = item.ingredient

        # total quantity needed
        qty_used = Decimal(item.qteUtilise) * Decimal(quantity)

        # current stock
        before = ingredient.stock
        after = before - qty_used

        if after < 0:
            raise Exception(
                f"Insufficient stock for {ingredient.nom}"
            )

        # update ingredient stock
        ingredient.stock = after
        ingredient.save()

        # create movement log
        StockMovement.objects.create(
            ingredient=ingredient,
            movement_type="SALE",
            quantity=-qty_used,
            stock_before=before,
            stock_after=after,
            reference_id=vente_id,
            reference_model="Vente"
        )