from django.urls import path
from .views import PatientGenericAPIView, DoctorGenericAPIView

app_name = 'api'

urlpatterns = [
    path('patient/<int:pk>/', PatientGenericAPIView.as_view(), name='get_patient'),
    path('patient/', PatientGenericAPIView.as_view(), name='get_patient'),
    path('doctor/<int:pk>/', DoctorGenericAPIView.as_view(), name='get_doctor'),
    path('doctor/', DoctorGenericAPIView.as_view(), name='get_doctor'),
]
