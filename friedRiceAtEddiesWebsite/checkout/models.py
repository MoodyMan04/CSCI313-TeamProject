from django.db import models
from main.models import Menu, Way_Recieved

# Create your models here.
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    tokens = models.IntegerField()
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=31)
    email = models.EmailField()
    address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.username}, {self.fname} {self.lname}'
    
class CartItem(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.quantity} x {self.item.name}'
    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    way_recieved_id = models.ForeignKey(Way_Recieved, on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(Menu)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    is_completed = models.BooleanField()
    is_cash = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.id}, {self.member_id}, {self.way_recieved_id}'