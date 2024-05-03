from django.db import models
from main.models import Menu, Way_Recieved
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tokens = models.IntegerField()
    phone_num = models.CharField(max_length=31)
    mailing_address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.user}'
    
class CartItem(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.quantity} x {self.item.name}'
    
class OrderLine(models.Model):
    id = models.AutoField(primary_key=True)
    menu_item = models.ForeignKey(Menu, on_delete=models.DO_NOTHING)
    qty = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f'{self.qty}x {self.menu_item}'
    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    way_recieved_id = models.ForeignKey(Way_Recieved, on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(OrderLine)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    is_completed = models.BooleanField()
    is_cash = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.id}, {self.member_id}, {self.way_recieved_id}'
