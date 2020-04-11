from django.shortcuts import render
from rest_framework import viewsets
from .models import Opportunity
from .serializers import *

# Create your views here.
class OpportunityView(viewsets.ModelViewSet):
    """
    list:
    Returns the list of Oportunity.

    create:
    Creates a Oportunity.

    destroy:
    Removes the selected Oportunity.
    """        
    serializer_class = OpportunitiesSerializer

    def get_queryset(self):
        return Opportunity.objects.all()