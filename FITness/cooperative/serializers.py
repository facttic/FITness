from rest_framework import serializers
from .models import Cooperative


class CooperativeSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='status_description', read_only=True)

    class Meta:
        model = Cooperative
        fields = ('name', 'status')
