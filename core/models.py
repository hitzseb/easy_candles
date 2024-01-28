from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=45)
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.ticker} | {self.name}'