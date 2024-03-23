from django.db import models

# Create your models here.

class Inventory(models.Model):
    id = models.BigAutoField(primary_key=True)
    isbn_id = models.CharField(max_length=255,unique=True)
    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.BooleanField(default=True)
    quantity = models.IntegerField()
    author = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title