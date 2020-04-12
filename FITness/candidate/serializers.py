from rest_framework import serializers
from .models import Technology, Candidate


class TechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = Technology 
        fields = ('pk', 'name')


class CandidatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate 
        fields = ('name', 'english_level', 'availability')
