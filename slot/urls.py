from django.urls import path
from .views import  SlotDetail, SlotList

urlpatterns = [

    path('', SlotList.as_view(), name="all slots" ),
    path('<int:pk>', SlotDetail.as_view(), name="slot")

]