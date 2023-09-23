from django.db import models
from custom_users.models import CustomUser

class Customer(models.Model):
   
    user = models.OneToOneField(CustomUser, related_name="customer", primary_key=True, on_delete=models.CASCADE )
    customer_name = models.CharField(max_length=100)
    pickup_location = models.CharField(max_length=100)
    drop_off_location = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name
