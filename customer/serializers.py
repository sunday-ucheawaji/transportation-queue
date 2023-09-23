from rest_framework import serializers
from .models import Customer
from custom_users.serializers import CustomUserSerializer


class CustomerSerializer(serializers.ModelSerializer):

    # user = CustomUserSerializer()

    class Meta:

        model= Customer
        fields = "__all__"
        # exclude= ["user", ]

