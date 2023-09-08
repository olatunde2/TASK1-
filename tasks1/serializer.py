from rest_framework import serializers

class Datetimeserializer(serializers.Serializer):
    current_date = serializers.DateField(format="%Y-%m-%dT%H:%M:%SZ")
