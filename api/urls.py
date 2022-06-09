from django.urls import path
from .views import GetPatientInfo, GetDoctorInfo

app_name = 'api'

urlpatterns = [
    path('patient/<int:pk>/', GetPatientInfo.as_view(), name='get_patient'),
    path('patient/', GetPatientInfo.as_view(), name='get_patient'),
    path('doctor/<int:pk>/', GetDoctorInfo.as_view(), name='get_doctor'),
    path('doctor/', GetDoctorInfo.as_view(), name='get_doctor'),
]
