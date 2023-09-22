from django.urls import path
from .views import CustomUserList, CustomUserDetail

urlpatterns = [
    path('', CustomUserList.as_view(), name='all_users'),
    path('<int:pk>', CustomUserDetail.as_view(), name='user'),

]