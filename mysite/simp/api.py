from rest_framework import generics, permissions
from .serializers import PatientSerializer
from .models import Patient

class PatientList(generics.ListAPIView):
  def get_queryset(self):
    return Patient.objects.all()
  serializer_class = PatientSerializer
#     queryset  = User
#     permission_classes = [
#         permissions.AllowAny
#     ]


class PatientDetail(generics.RetrieveAPIView):
  def get_queryset(self):
    return Patient.objects.all()
  serializer_class = PatientSerializer
  lookup_field = 'clean_patient_name'

#     queryset  = User

