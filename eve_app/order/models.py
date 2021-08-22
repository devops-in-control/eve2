from django.db import models

class OrderForm(models.Model):
    
    email = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
