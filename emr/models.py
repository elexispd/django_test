from django.db import models
from django.contrib.auth.models import User
from encrypted_model_fields.fields import *
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password





class Department(models.Model) :
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    

class StaffManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        
        # Set the password to 'password1' if not provided
        if password is None:
            password = 'password1'
        
        # Hash the password
        user.set_password(password)
        
        # Save the user
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superadmin', True)

        if extra_fields.get('is_superadmin') is not True:
            raise ValueError('Superuser must have is_superadmin=True.')

        return self.create_user(email, password, **extra_fields)




class Staff(AbstractBaseUser) :
    first_name = EncryptedCharField(max_length=200)
    last_name = EncryptedCharField(max_length=200)
    email = models.CharField(max_length=100, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    phone_number =  models.CharField(max_length=20, unique=True)
    doctor_type = EncryptedCharField(max_length=200) # Contract or Permanent
    doctor_specialization = EncryptedCharField(max_length=200)
    is_superadmin = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    objects = StaffManager()  # Attach StaffManager to Staff model

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',  'phone_number']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.department} {self.phone_number} {self.doctor_type} {self.doctor_specialization} {self.is_superadmin}  {self.created_at} {self.updated_at}"



class Patient(models.Model) :
    first_name = EncryptedCharField(max_length=200)
    last_name = EncryptedCharField(max_length=200)
    phone_number = EncryptedCharField(max_length=200)
    dob = EncryptedCharField(max_length=200)
    next_of_kin = EncryptedCharField(max_length=200)
    address_of_kin = EncryptedTextField(max_length=200)
    place_of_origin = EncryptedCharField(max_length=200)
    mswd = EncryptedCharField(max_length=200, null=True, blank=True)
    xray_number = EncryptedCharField(max_length=200, null=True, blank=True)
    ethnic_group = EncryptedCharField(max_length=200, null=True, blank=True)
    occupation = EncryptedCharField(max_length=200, null=True, blank=True)
    religion = EncryptedCharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        # {self.phone_number} {self.dob} {self.next_of_kin} {self.address_of_kin} {self.place_of_origin} {self.mswd} {self.xray_number} {self.ethnic_group} {self.occupation} {self.religion} {self.created_at} {self.updated_at}"


class MedicalRecord(models.Model) :
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    blood_group = EncryptedCharField(max_length=200)
    genotype = EncryptedCharField(max_length=200)
    diagnoses = EncryptedTextField(max_length=2000)
    admitted_at = models.DateTimeField(auto_now_add=True)
    discharged_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.patient} {self.doctor} {self.blood_group} {self.genotype} {self.diagnoses} {self.admitted_at} {self.discharged_at}  {self.updated_at}"
    
    
class Billing(models.Model) :
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    amount = EncryptedCharField(max_length=200)
    description = EncryptedCharField(max_length=200)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.patient} {self.amount} {self.status}  {self.created_at}  {self.updated_at}"
    
 

class Drug(models.Model) :
    name = EncryptedCharField(max_length=200)
    price  = EncryptedCharField(max_length=200)
    quantity =  EncryptedCharField(max_length=200) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} {self.price} {self.quantity}  {self.created_at}  {self.updated_at}"


    
class Prescription(models.Model) :
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    vital_signs = EncryptedTextField(max_length=2000, null=True, blank=True)
    complaint = EncryptedTextField(max_length=2000, null=True, blank=True)
    diagnosis = EncryptedTextField(max_length=2000, null=True, blank=True)
    examination = EncryptedTextField(max_length=2000, null=True, blank=True)
    plan = EncryptedTextField(max_length=2000, null=True, blank=True)
    medication_details = models.JSONField()
    others = EncryptedTextField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.patient} {self.doctor} {self.vital_signs} {self.complaint}  {self.examination} {self.plan} {self.medication_details}  {self.others} {self.created_at}  {self.updated_at}"
    
    
class LabTest(models.Model) :
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    name = EncryptedCharField(max_length=200)
    description = EncryptedTextField()
    status = models.BooleanField(default=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.patient}"
    

class LabResult(models.Model) :
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    test = models.ForeignKey(LabTest, on_delete=models.SET_NULL, null=True)
    result = EncryptedTextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.patient}"


class Appointment(models.Model) :
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, related_name='doctor_appointments')
    status = models.BooleanField(default=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.patient}"



class PrescribedMedication(models.Model):
    prescription = models.ForeignKey(Prescription, related_name='prescribed_medications', on_delete=models.SET_NULL, null=True, blank=True)
    vital_signs = EncryptedTextField(max_length=2000, null=True, blank=True)
    complaint = EncryptedTextField(max_length=2000, null=True, blank=True)
    diagnosis = EncryptedTextField(max_length=2000, null=True, blank=True)
    examination = EncryptedTextField(max_length=2000, null=True, blank=True)
    plan = EncryptedTextField(max_length=2000, null=True, blank=True)
    drug = models.ForeignKey(Drug, on_delete=models.SET_NULL, null=True, blank=True)
    dosage = EncryptedCharField(max_length=200, null=True, blank=True)
    frequency = EncryptedCharField(max_length=200, null=True, blank=True)
    duration = EncryptedCharField(max_length=200, null=True, blank=True)
    others = EncryptedTextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.prescription} {self.vital_signs} {self.complaint}  {self.examination} {self.plan} {self.drug} {self.dosage}  {self.frequency} {self.duration}  {self.others}"

