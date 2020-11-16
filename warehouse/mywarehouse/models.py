from django.db import models

class Inflow(models.Model):
    name = models.CharField(max_length=200, help_text="Goods Name")
    quantity = models.PositiveIntegerField()
    comment = models.TextField(help_text="Discribe the delivery")

    def __str__(self):
        return f'{self.name}, {self.quantity}'

class Outflow(models.Model):
    name = models.CharField(max_length=200, help_text="Goods Name")
    quantity = models.PositiveIntegerField()
    comment = models.TextField(help_text="Discribe the Destination")

    def __str__(self):
        return f'{self.name}, {self.quantity}'