from rest_framework import serializers

class Datetimeserializer(serializers.Serializer):
    current_date = serializers.DateField(format="2023-09-08T%H:%M:%SZ")
