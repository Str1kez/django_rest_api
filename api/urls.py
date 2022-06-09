from django.urls import path
from .views import PatientAPIView, DoctorAPIView

app_name = 'api'

urlpatterns = [
    path('patient/<int:pk>/', PatientAPIView.as_view(), name='get_patient'),
    path('patient/', PatientAPIView.as_view(), name='get_patient'),
    path('doctor/<int:pk>/', DoctorAPIView.as_view(), name='get_doctor'),
    path('doctor/', DoctorAPIView.as_view(), name='get_doctor'),
]
