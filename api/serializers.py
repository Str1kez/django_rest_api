from typing import OrderedDict

from django.db.models import QuerySet
from rest_framework import serializers

from .exceptions import ExistsInDatabase
from .models import Patient, Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class __PatientsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Patient
            fields = ['name', 'address', 'district', 'phone_number']

    patients = __PatientsSerializer(many=True, allow_null=True)

    class Meta:
        model = Doctor
        fields = ['name', 'post', 'phone_number', 'patients']

    def create(self, validated_data: OrderedDict) -> Doctor:
        data = {el: self.initial_data[el] for el in self.validated_data if el != 'patients'}
        return Doctor.objects.create(**data)

    def update(self, instance: QuerySet, validated_data: OrderedDict):
        pass

    def validate(self, attrs: OrderedDict) -> OrderedDict:
        data = {el: self.initial_data[el] for el in self.initial_data if el != 'patients'}
        existing_doctor_queryset = Doctor.objects.filter(**data)  # Можно заменить на get
        if existing_doctor_queryset:
            raise ExistsInDatabase
        return attrs


class PatientSerializer(serializers.ModelSerializer):
    class __DoctorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Doctor
            fields = ['name', 'post', 'phone_number']

    doctor = __DoctorSerializer(allow_null=True)

    class Meta:
        model = Patient
        fields = ['name', 'address', 'district', 'phone_number', 'doctor']

    def create(self, validated_data: OrderedDict) -> Patient:
        doctor = validated_data.pop('doctor')
        if doctor is not None:
            doctor_query_set = Doctor.objects.filter(**doctor)  # Можно заменить на get
            if doctor_query_set:
                doctor = doctor_query_set[0]
            else:
                doctor = Doctor.objects.create(**doctor)
        return Patient.objects.create(doctor=doctor, **validated_data)

    def update(self, instance: QuerySet, validated_data: OrderedDict):
        pass

    def validate(self, attrs) -> OrderedDict:
        doctor_attrs = self.initial_data.get('doctor')
        patient_attrs = {el: self.initial_data.get(el) for el in self.initial_data if el != 'doctor'}
        if doctor_attrs:
            doctor_attrs = {'doctor__' + el: doctor_attrs[el] for el in doctor_attrs}
            query_set = Patient.objects.filter(**patient_attrs, **doctor_attrs)
        else:
            query_set = Patient.objects.filter(**patient_attrs, doctor=None)
        if query_set:
            raise ExistsInDatabase
        return attrs
