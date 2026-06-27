from django.db import models

class Bilan(models.Model):
    date = models.DateField(unique=True)

    revenue = models.DecimalField(max_digits=12, decimal_places=2)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    profit = models.DecimalField(max_digits=12, decimal_places=2)
