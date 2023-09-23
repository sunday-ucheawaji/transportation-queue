from rest_framework import serializers
from slot.models import Slot
from customer.serializers import CustomerSerializer


class SlotSerializer(serializers.ModelSerializer):


    class Meta:
        model = Slot
        fields = "__all__"

    def create(self, validated_data):
        slot = Slot.objects.create(**validated_data)
        return slot