from rest_framework import generics
from slot.models import Slot
from slot.serializers import SlotSerializer

# Create your views here.
class SlotList(generics.ListCreateAPIView):
    queryset = Slot.objects.all()
    serializer_class= SlotSerializer


class SlotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Slot.objects.all()
    serializer_class= SlotSerializer
  