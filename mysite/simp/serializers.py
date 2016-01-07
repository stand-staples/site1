from rest_framework import serializers
from simp.models import Patient, Payment, Treatment

class PatientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Patient
    fields = ('patient_name','default_price','is_archived','is_deleted','clean_patient_name',)

class PaymentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Payment
    fields = ('patient', 'payment_date', 'comments', 'amount', 'receipt_num', 'is_deleted',)

class TreatmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Treatment
    fields = ('patient', 'treatment_date', 'comments', 'price', 'is_deleted', )

#     TODO:
#     serializers.HyperlinkedModelSerializer