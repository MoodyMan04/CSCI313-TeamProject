from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tokens = models.IntegerField()
    phone_num = models.CharField(max_length=31)
    mailing_address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.id) + ", " + str(self.user)