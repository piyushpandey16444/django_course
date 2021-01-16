from django.db import models


class CurrencyValue(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    symbole = models.CharField(max_length=255, null=False, unique=True)
    value = models.FloatField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
