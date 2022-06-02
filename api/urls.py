from django.urls import path
from views import GetPatientInfo

app_name = 'api'

urlpatterns = [
    path('get/patient', GetPatientInfo.as_view(), name='get_patient'),
]
