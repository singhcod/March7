from django.shortcuts import render

# Create your views here.
from .models import student
from .serializers import Studentserializers
from rest_framework import generics


class GenericLists(generics.ListCreateAPIView):
    queryset =student .objects.all()
    serializer_class = Studentserializers


class GenericDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = Studentserializers