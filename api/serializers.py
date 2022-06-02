from rest_framework import serializers

from .models import Patient, Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class __PatientsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Patient
            fields = ['name', 'address', 'district', 'phone_number']

    patients = __PatientsSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ['name', 'post', 'phone_number', 'patients']


class PatientSerializer(serializers.ModelSerializer):
    class __DoctorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Doctor
            fields = ['name', 'post', 'phone_number']

    doctor = __DoctorSerializer(read_only=True)

    class Meta:
        model = Patient
        fields = ['name', 'address', 'district', 'phone_number', 'doctor']
