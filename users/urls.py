from django.urls import path
from .views import UserListCreateApiView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('users/', UserListCreateApiView.as_view(), name='users_list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user_id'),
]
