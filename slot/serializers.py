from rest_framework import serializers
from slot.models import Slot


class SlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slot
        fields = "__all__"
