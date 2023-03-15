from .models import Text
from rest_framework import serializers


class textSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'