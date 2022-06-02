from django.urls import path
from .views import GetPatientInfo, GetDoctorInfo

app_name = 'api'

urlpatterns = [
    path('get/patient', GetPatientInfo.as_view(), name='get_patient'),
    path('get/doctor', GetDoctorInfo.as_view(), name='get_doctor'),
]
