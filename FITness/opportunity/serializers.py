from rest_framework import serializers
from .models import Opportunity


class OpportunitiesSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client.name', read_only=True)
    mode = serializers.CharField(source='mode_description', read_only=True)

    class Meta:
        model = Opportunity 
        fields = ('client', 'mode', 'mandatory_english', 'more_info', 'rate', 'date')
