from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from server.serializers import CoursSerializer
from server.models import Cours

# Create your views here.

class ListCoursAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer

class CreateCoursAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer

class UpdateCoursAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer

class DeleteCoursAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer
