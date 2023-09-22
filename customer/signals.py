# signals.py

from django.dispatch import receiver, Signal



custom_user_signal = Signal(['user', 'customer_name', "pickup_location", "drop_off_location"])


