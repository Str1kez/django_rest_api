from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Patient
from .serializers import PatientSerializer


class GetPatientInfo(APIView):
    def get(self, request):
        patient_name = request.GET.get('name')
        if patient_name:
            patient = get_object_or_404(Patient, name=patient_name)
        else:
            patient = Patient.objects.first()
        patient_serializer = PatientSerializer(instance=patient, many=False)
        return Response(patient_serializer.data)
