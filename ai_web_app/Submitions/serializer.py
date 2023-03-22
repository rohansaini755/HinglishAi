from rest_framework import serializers
from Submitions.models import submition



class submition_serializer(serializers.ModelSerializer):
    class Meta:
        model = submition
        fields= '__all__'