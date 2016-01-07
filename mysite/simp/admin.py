from django.contrib import admin
from .models import Patient, Payment, Treatment
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
  list_display = ['patient_name','default_price','is_archived','is_deleted']
  class Meta:
      model = Patient

class TreatmentAdmin(admin.ModelAdmin):
  list_display = ['patient', 'treatment_date', 'comments', 'price', 'is_deleted']
  class Meta:
      model = Treatment

class PaymentAdmin(admin.ModelAdmin):
  list_display = [ 'patient','payment_date', 'comments', 'amount', 'receipt_num', 'is_deleted']
  class Meta:
      model = Payment

# admin.site.register(mymodels, admin.ModelAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Payment, PaymentAdmin)
