# sales/services.py

from inventory.services import deduct_stock_for_sale
from menu.models import Plat


def process_vente(vente):
    for item in vente.items.all():
        deduct_stock_for_sale(
            plat=item.plat,
            quantity=item.qtePlat,
            vente_id=vente.idVente
        )