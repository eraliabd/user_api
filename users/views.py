from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from .models import User, Person
from .serializers import UserSerializer, PersonSerializer


# class UserListCreateApiView(GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     parser_classes = [FormParser, MultiPartParser]
#
#     def get(self, request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class UserRetrieveUpdateDestroyAPIView(GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     parser_classes = [FormParser, MultiPartParser]
#
#     def get(self, request, pk):
#         queryset = get_object_or_404(User, pk=pk)
#         serializer = UserSerializer(queryset)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         queryset = get_object_or_404(User, pk=pk)
#         serializer = UserSerializer(queryset, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         queryset = get_object_or_404(User, pk=pk)
#         queryset.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class UserListCreateApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated, )
    parser_classes = [FormParser, MultiPartParser]

    # def perform_create(self, serializer):
    #     self.request.data.get('username', None)
    #     if self.request.user.is_authenticated:
    #         instance = serializer.save(username=self.request.user)
    #     else:
    #         instance = serializer.save()


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [FormParser, MultiPartParser]


class PersonListCreateApiView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    parser_classes = [FormParser, MultiPartParser]

    # def perform_create(self, serializer):
    #     queryset = Person.objects.filter(owner=self.request.user)
    #     if queryset.exists():
    #         raise ValidationError('You have already signed up')
    #     serializer.save()

