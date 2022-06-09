from typing import Union, Type

from rest_framework.exceptions import NotFound
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import permissions

from .models import Patient, Doctor
from .serializers import PatientSerializer, DoctorSerializer


class PersonAPIView(APIView):
    permission_classes = permissions.IsAuthenticated,
    serializer: Type[Union[PatientSerializer, DoctorSerializer]] = None
    model: Union[Patient, Doctor] = None

    def get(self, request: Request, pk: int = None) -> Response:
        person_name = request.GET.get('name')
        if pk is not None:
            person = get_object_or_404(self.model, pk=pk)
        elif person_name:
            """
            Можно было использовать icontains, но с SQLite работает non-ASCII в sensitive всегда
            https://docs.djangoproject.com/en/4.0/ref/databases/#sqlite-string-matching
            """
            person = self.model.objects.filter(name=person_name)
        else:
            person = self.model.objects.all()
        person_serializer = self.serializer(instance=person, many=pk is None)
        return Response(person_serializer.data)

    def post(self, request: Request) -> Response:
        serialized_data = self.serializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
        return Response(request.data)

    def put(self, request: Request) -> Response:
        """TODO: Develop this method"""
        if True:
            raise NotFound(detail='DB doesn`t have this item')
        return Response(request.data)


class PatientAPIView(PersonAPIView):
    serializer = PatientSerializer
    model = Patient


class DoctorAPIView(PersonAPIView):
    serializer = DoctorSerializer
    model = Doctor
