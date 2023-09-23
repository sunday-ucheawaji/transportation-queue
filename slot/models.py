from django.db import models
from customer.models import Customer


class Slot(models.Model):
    date = models.DateField()
    slot_1 = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL, related_name='slot_1')
    slot_2 = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL, related_name='slot_2')
    slot_3 = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL, related_name='slot_3')
    slot_4 = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL, related_name='slot_4')

    def __str__(self):
        return str(self.date)
