from rest_framework import viewsets
from .serializers import *


class TechnologyView(viewsets.ModelViewSet):
    """
    list:
    Returns the list of Technologies.

    create:
    Creates a Technology.

    destroy:
    Removes the selected Technology.
    """        
    serializer_class = TechnologySerializer

    def get_queryset(self):
        return Technology.objects.all()


class CandidateView(viewsets.ModelViewSet):
    """
    list:
    Returns the list of Candidates.

    create:
    Creates a Candidate.

    destroy:
    Removes the selected Candidate.
    """        
    serializer_class = CandidatesSerializer

    def get_queryset(self):
        return Candidate.objects.all()
