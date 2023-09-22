from django.db import models
from custom_users.models import CustomUser

class Customer(models.Model):
    customer_id = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    pickup_location = models.CharField(max_length=100)
    drop_off_location = models.CharField(max_length=100)
    user = models.OneToOneField(CustomUser, related_name="customer",  null=True, blank=True, on_delete=models.CASCADE )

    def __str__(self):
        return self.customer_name

class Slot(models.Model):
    date = models.DateField()
    slot_1 = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL, related_name='slot_1')
    slot_2 = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL, related_name='slot_2')
    slot_3 = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL, related_name='slot_3')
    slot_4 = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL, related_name='slot_4')

    def __str__(self):
        return str(self.date)