from rest_framework import serializers
from .models import APITable


class APITableSerializer(serializers.ModelSerializer):
    class Meta:
        model = APITable
        fields = '__all__'
