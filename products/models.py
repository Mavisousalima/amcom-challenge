from django.db import models


class Product(models.Model):
    """
    Representa um produto na papelaria hipotética.
    """
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    commission_rate = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        """
        Retorna a descrição do produto como representação em string.
        """
        return self.description