from rest_framework import serializers
from .models import Technology, Candidate


class TechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = Technology 
        fields = ('pk', 'name')


class CandidatesSerializer(serializers.ModelSerializer):
    english_level = serializers.CharField(source='english_level_description', read_only=True)
    availability = serializers.CharField(source='availability_description', read_only=True)

    class Meta:
        model = Candidate 
        fields = ('name', 'english_level', 'availability')
