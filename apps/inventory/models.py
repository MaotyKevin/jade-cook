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