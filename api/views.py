from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Patient, Doctor
from .serializers import PatientSerializer, DoctorSerializer


class GetPatientInfo(APIView):
    def get(self, request):
        patient_name = request.GET.get('name')
        if patient_name:
            patient = get_object_or_404(Patient, name=patient_name)
        else:
            patient = Patient.objects.first()
        patient_serializer = PatientSerializer(instance=patient, many=False)
        return Response(patient_serializer.data)


class GetDoctorInfo(APIView):
    def get(self, request):
        doctor_name = request.GET.get('name')
        if doctor_name:
            doctor = get_object_or_404(Doctor, name=doctor_name)
        else:
            doctor = Doctor.objects.first()
        doctor_serializer = DoctorSerializer(instance=doctor, many=False)
        return Response(doctor_serializer.data)
