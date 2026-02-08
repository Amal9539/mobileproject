from django.db import models

# Create your models here.
class Login(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    def __str__(self):
        return self.Username

class User(models.Model):
    phonemodel = models.CharField(max_length=100)
    imeino = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    complaint = models.TextField()
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    actual_price = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return self.customer_name