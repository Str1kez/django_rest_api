from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer

# Create your views here.
from models import Patient


class GetPatientInfo(APIView):
    def get(self, request):
        patient = Patient.objects.first()
        serializer = ModelSerializer(instance=patient)
        return Response(serializer.data)
