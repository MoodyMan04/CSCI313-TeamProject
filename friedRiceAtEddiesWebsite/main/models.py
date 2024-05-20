from django.db import models

# Create your models here.
class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.name}'

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.name}'

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self) -> str:
        return f'{self.id}'

class Way_Recieved(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.type}'