from django.forms import model_to_dict
from rest_framework.exceptions import NotFound
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import permissions

from .models import Patient, Doctor
from .serializers import PatientSerializer, DoctorSerializer


class GetPatientInfo(APIView):
    permission_classes = permissions.IsAuthenticated,

    def get(self, request: Request) -> Response:
        patient_name = request.GET.get('name')
        if patient_name:
            patient = get_object_or_404(Patient, name=patient_name)
        else:
            patient = Patient.objects.first()
        patient_serializer = PatientSerializer(instance=patient, many=False)
        return Response(patient_serializer.data)

    def post(self, request: Request) -> Response:
        serialized_data = PatientSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            pass
            # serialized_data.save()
        return Response(request.data)

    def put(self, request: Request) -> Response:
        if True:
            raise NotFound(detail='DB doesn`t have this item')
        return Response(request.data)


class GetDoctorInfo(APIView):
    def get(self, request: Request) -> Response:
        doctor_name = request.GET.get('name')
        if doctor_name:
            doctor = get_object_or_404(Doctor, name=doctor_name)
        else:
            doctor = Doctor.objects.first()
        doctor_serializer = DoctorSerializer(instance=doctor, many=False)
        return Response(doctor_serializer.data)

    def post(self, request: Request) -> Response:
        pass
