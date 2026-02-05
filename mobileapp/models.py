from django.db import models

# Create your models here.
class Login(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    def __str__(self):
        return self.Username

class User(models.Model):
    phonemodel = models.CharField(max_length=100)
    imeino = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    complaint = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)


    def __str__(self):
        return self.customer_name
