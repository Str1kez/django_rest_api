from rest_framework import serializers


class PatientSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=100)
    district = serializers.IntegerField()
    phone_number = serializers.CharField(max_length=11, allow_null=True)
    doctor = serializers.CharField(source='doctor.name')
