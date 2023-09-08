from rest_framework import serializers

class Datetimeserializer(serializers.Serializer):
    current_date = serializers.DateField(format="%Y-%m-%d")
    current_time = serializers.TimeField(format="T%H:%M:%SZ")
