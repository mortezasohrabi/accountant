from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Token(models.Model):
    user=models.OneToOneField(User , on_delete = models.CASCADE)
    token=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user}_token"

class Expense(models.Model):
    text = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.text } "
class Income(models.Model):
    text = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.text}"
