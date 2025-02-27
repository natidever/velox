
from django.db import models

class Users(models.Model):
    user_id=models.BigIntegerField(primary_key=True)

class Wallet(models.Model):
    user=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='wallets')
    wallet_address=models.CharField(max_length=44)
    private_key=models.CharField(max_length=128)


