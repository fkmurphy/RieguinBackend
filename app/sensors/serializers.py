from rest_framework import serializers

class SensorSerializer(serializers.Serializer):
    name = serializers.CharField()

