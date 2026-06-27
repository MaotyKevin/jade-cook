# accounting/services.py

from decimal import Decimal
from django.db.models import Sum
from datetime import date

from sales.models import Vente
from inventory.models import StockMovement


def compute_daily_bilan(target_date):

    # 1. REVENUE
    ventes = Vente.objects.filter(date__date=target_date)

    revenue = sum(
        v.total for v in ventes
    )

    # 2. COST (from stock movements)
    cost_movements = StockMovement.objects.filter(
        created_at__date=target_date,
        movement_type="SALE"
    )

    cost = sum(
        abs(m.quantity) * m.ingredient.prixUnit
        for m in cost_movements
    )

    # 3. PROFIT
    profit = revenue - cost

    return {
        "date": target_date,
        "revenue": revenue,
        "cost": cost,
        "profit": profit
    }