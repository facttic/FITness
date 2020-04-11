# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import render

from .models import Technology
from .serializers import *

class TechnologyView(viewsets.ModelViewSet):
    """
    list:
    Returns the list of Technologies.

    create:
    Creates a Technology for the current cooperative.

    destroy:
    Removes the selected Technology.
    """        
    serializer_class = TechnologySerializer

    def get_queryset(self):
        return Technology.objects.all()
