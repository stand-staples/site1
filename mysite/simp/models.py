from django.db import models

# Create your models here.

class Patient(models.Model):
  patient_name = models.CharField( max_length=200, unique = True)
  default_price = models.IntegerField()
  is_archived = models.BooleanField(default=False)
  is_deleted = models.BooleanField(default=False)
  is_ok = models.BooleanField(default=False)
  clean_patient_name = models.CharField( max_length=200, unique = False)
  def __str__(self):
    return u'%s' %self.patient_name
  
  def save(self, *args, **kwargs):
    if self.patient_name: 
      a = ' '.join(self.patient_name.split())
      self.patient_name = a
      a = a.replace(" ","_")
      self.clean_patient_name = a
    super(Patient, self).save(*args, **kwargs)

    
    
class Payment(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  payment_date = models.DateField()
  comments = models.CharField(max_length=200)
  amount = models.IntegerField()
  receipt_num = models.IntegerField()
  is_deleted = models.BooleanField(default=False)
  def __str__(self):
    return u'%s' %self.receipt_num

class Treatment(models.Model):
  patient = models.ForeignKey( Patient, on_delete=models.CASCADE )
  treatment_date = models.DateField()
  comments = models.CharField(max_length=200)
  price = models.IntegerField()
  is_deleted = models.BooleanField(default=False)
  def __str__(self):
    return u'%s' %self.patient.patient_name
