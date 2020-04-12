from rest_framework import viewsets

from FITness.cooperative.models import Cooperative
from FITness.cooperative.serializers import CooperativeSerializer


class CooperativeView(viewsets.ModelViewSet):
    """
    list:
    Returns the list of Technologies.

    create:
    Creates a Technology.

    destroy:
    Removes the selected Technology.
    """        
    serializer_class = CooperativeSerializer

    def get_queryset(self):
        return Cooperative.objects.all()
