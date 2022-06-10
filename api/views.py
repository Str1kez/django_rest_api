from typing import Union

from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.request import Request

from .models import Patient, Doctor
from .serializers import PatientSerializer, DoctorSerializer


class BaseGenericAPIView(RetrieveModelMixin,
                         ListModelMixin,
                         CreateModelMixin,
                         GenericAPIView):
    model: Union[Patient, Doctor] = None
    serializer_class: Union[PatientSerializer, DoctorSerializer] = None
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: Request, *args, **kwargs):
        person_id = kwargs.get('pk')
        person_name = request.query_params.get('name')
        if person_id is not None:
            return self.retrieve(request, *args, **kwargs)
        if person_name is not None:
            self.queryset = self.model.objects.filter(name=person_name)
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        if self.queryset is not None:
            return self.queryset
        if self.model is not None:
            return self.model.objects.all()
        return self.queryset


class PatientGenericAPIView(BaseGenericAPIView):
    model = Patient
    serializer_class = PatientSerializer


class DoctorGenericAPIView(BaseGenericAPIView):
    model = Doctor
    serializer_class = DoctorSerializer
