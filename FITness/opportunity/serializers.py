from rest_framework import serializers
from .models import Opportunity


class OpportunitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Opportunity 
        fields = ('client', 'mode', 'mandatory_english', 'more_info', 'rate', 'date')
