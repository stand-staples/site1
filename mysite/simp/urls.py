from django.conf.urls import include, url
from . import views

from .api import PatientList, PatientDetail

patients_urls = [
    url(r'^/$', PatientList.as_view(), name='patient-list'),
    url(r'^/(?P<clean_patient_name>[\u0590-\u05FFa-zA-Z0-9_.-]+)$', PatientDetail.as_view(), name='patient-detail'),
]

urlpatterns = [
    url(r'^patients', include(patients_urls)),
]



