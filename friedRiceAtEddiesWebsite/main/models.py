from django.db import models
from checkout import models as checkout_models

# Create your models here.
class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.name)

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return str(self.name)

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self) -> str:
        return str(self.id)
    

class Way_Recieved(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.type)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey(checkout_models.Member, on_delete=models.CASCADE, null=True, blank=True)
    way_recieved_id = models.ForeignKey(Way_Recieved, on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(Menu)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    is_completed = models.BooleanField()
    is_cash = models.BooleanField()

    def __str__(self) -> str:
        return str(self.id) + ", " + str(self.member_id) + ", " + str(self.way_recieved_id)
  