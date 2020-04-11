from rest_framework import serializers
from .models import Opportunity

class OpportunitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Opportunity 
        fields = ('pk', 'client', 'mode', 'candidates_qty', 'mandatory_english', 'more_info', 'rate', 'date')
