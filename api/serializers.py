from typing import OrderedDict

from django.db.models import QuerySet
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

    doctor = __DoctorSerializer(allow_null=True)

    class Meta:
        model = Patient
        fields = ['name', 'address', 'district', 'phone_number', 'doctor']

    def create(self, validated_data: OrderedDict) -> Patient:
        doctor = validated_data.pop('doctor')
        # TODO:  Написать чекер на существующего доктора в бд
        if doctor is not None:
            doctor = Doctor.objects.create(**doctor)
        return Patient.objects.create(doctor=doctor, **validated_data)

    def update(self, instance: QuerySet, validated_data: OrderedDict):
        pass

    def validate(self, attrs) -> bool:
        doctor_attrs = self.initial_data.get('doctor')
        attrs = {el: self.initial_data.get(el) for el in self.initial_data if el != 'doctor'}
        if doctor_attrs:
            doctor_attrs = {'doctor__' + el: doctor_attrs[el] for el in doctor_attrs}
            query_set = Patient.objects.filter(**attrs, **doctor_attrs)
        else:
            query_set = Patient.objects.filter(**attrs, doctor=None)
        if query_set:
            raise serializers.ValidationError('Patient exists in database')
        return True
