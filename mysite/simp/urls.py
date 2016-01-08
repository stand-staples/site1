from django.conf.urls import include, url
from django.views.generic.base import TemplateView

from . import views
from .api import PatientList, PatientDetail

patients_urls = [
    url(r'^/$', PatientList.as_view(), name='patient-list'),
    url(r'^/(?P<clean_patient_name>[\u0590-\u05FFa-zA-Z0-9_.-]+)$', PatientDetail.as_view(), name='patient-detail'),
]

urlpatterns = [
    url(r'^index/$', views.index_view, name = "index-view"),
    url(r'^index2/$', TemplateView.as_view(template_name="simp/base.html"), name = "base-view"),
  
    url(r'^patients', include(patients_urls)),
]



