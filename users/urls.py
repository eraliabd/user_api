from django.urls import path
from .views import UserListCreateApiView, UserRetrieveUpdateDestroyAPIView, PersonListCreateApiView

urlpatterns = [
    path('users/', UserListCreateApiView.as_view(), name='users_list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user_id'),
    path('person/', PersonListCreateApiView.as_view(), name='person_list'),
]
