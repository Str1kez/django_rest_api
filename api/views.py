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
    # serialaizer = - аналогично тому, что написано внизу
    # model = Patient - для перестройки в наследование

    def get(self, request: Request, pk: int = None) -> Response:
        patient_name = request.GET.get('name')
        if pk is not None:
            patient = get_object_or_404(Patient, pk=pk)
        elif patient_name:
            patient = Patient.objects.filter(name=patient_name)
        else:
            patient = Patient.objects.all()
        patient_serializer = PatientSerializer(instance=patient, many=pk is None)
        return Response(patient_serializer.data)

    def post(self, request: Request) -> Response:
        serialized_data = PatientSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
        return Response(request.data)

    def put(self, request: Request) -> Response:
        """TODO: Develop this method"""
        if True:
            raise NotFound(detail='DB doesn`t have this item')
        return Response(request.data)


class GetDoctorInfo(APIView):
    def get(self, request: Request, pk: int = None) -> Response:
        doctor_name = request.query_params.get('name')
        if pk is not None:
            doctor = get_object_or_404(Doctor, pk=pk)
        elif doctor_name:
            doctor = Doctor.objects.filter(name=doctor_name)
        else:
            doctor = Doctor.objects.all()
        doctor_serializer = DoctorSerializer(instance=doctor, many=pk is None)
        return Response(doctor_serializer.data)

    def post(self, request: Request) -> Response:
        serialized_data = DoctorSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
        return Response(request.data)

    def put(self, request: Request) -> Response:
        """TODO: Develop this method"""
        if True:
            raise NotFound(detail='DB doesn`t have this item')
        return Response(request.data)
