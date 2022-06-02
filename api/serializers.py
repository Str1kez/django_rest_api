from rest_framework import serializers


class PatientSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)

