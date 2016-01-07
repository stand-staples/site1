from django.contrib import admin

# Register your models here.
from .models import User, Post, Photo
# class PatientAdmin(admin.ModelAdmin):
#  list_display = ['patient_name','phone_number','default_price','comments']
#  class Meta:
#      model = Patient

# class TreatmentAdmin(admin.ModelAdmin):
#  list_display = ['patient','treatment_date','main_concern','price','comments']
#  class Meta:
#      model = Treatment


mymodels = [User, Post, Photo]

admin.site.register(mymodels, admin.ModelAdmin)

#admin.site.register(Patient, PatientAdmin)
#admin.site.register(Treatment, TreatmentAdmin)


