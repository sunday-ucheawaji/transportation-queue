from django.dispatch import receiver
from .signals import custom_user_signal
from .models import Customer


@receiver(custom_user_signal)
def handle_customer_creation(sender, user, customer_name, pickup_location, drop_off_location, **kwargs):
    customer = Customer.objects.create(user=user, customer_name=customer_name, pickup_location=pickup_location, drop_off_location=drop_off_location)
    print(customer)