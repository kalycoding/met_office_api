from rest_framework import serializers
from .models import MaxTemp

# Serializers define the API representation.
class MaxTempSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaxTemp
        fields = "__all__"
