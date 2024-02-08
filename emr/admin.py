from django.contrib import admin
from .models import *



class DepartmentAdmin(admin.ModelAdmin) :
    list_display = ('name',)
    


class PatientAdmin(admin.ModelAdmin) :
    list_display = ('first_name', 'last_name','dob', 'next_of_kin','phone_number', 'address_of_kin','place_of_origin', 'mswd', 'xray_number', 'ethnic_group', 'occupation', 'religion', 'created_at', 'updated_at')
    
class StaffAdmin(admin.ModelAdmin) :
    list_display = ('first_name', 'last_name', 'email', 'department','phone_number', 'doctor_type','doctor_specialization', 'is_superadmin', 'status', 'created_at', 'updated_at')
    
    
class MedicalRecordAdmin(admin.ModelAdmin) :
    list_display = ('patient_id', 'doctor_id','diagnoses', 'blood_group','genotype', 'admitted_at', 'discharged_at', 'updated_at')
    
    
class BillingAdmin(admin.ModelAdmin) :
    list_display = ('patient_id', 'amount', 'description', 'status', 'created_at', 'updated_at')
    
    
class PrescriptionAdmin(admin.ModelAdmin) :
    list_display = ('doctor', 'patient', 'vital_signs', 'complaint', 'examination', 'plan', 'medication_details',  'others',  'created_at', 'updated_at')
    
    
    
class DrugAdmin(admin.ModelAdmin) :
    list_display = ('name', 'price', 'quantity', 'created_at', 'updated_at')
    
    
    
class LabTestAdmin(admin.ModelAdmin) :
    list_display = ('patient', 'name', 'description', 'status', 'creator', 'created_at', 'updated_at')
    
    
    
class LabResultAdmin(admin.ModelAdmin) :
    list_display = ('patient', 'test', 'result', 'creator', 'created_at')
    


class AppointmentAdmin(admin.ModelAdmin) :
    list_display = ('patient', 'doctor', 'status', 'creator', 'created_at')


# class PrescriptionAdmin(admin.ModelAdmin) :
#     list_display = ('doctor_id', 'patient_id', 'vital_signs', 'complaint', 'examination', 'plan', 'medication',  'others')
    
    
    
# class PrescribedMedicationsAdmin(admin.ModelAdmin) :
#     list_display = ('vital_signs', 'complaint', 'examination', 'plan', 'drug_name', 'dosage', 'dosage', 'duration', 'others')
    
#     def drug_name(self, obj):
#         return obj.drug.name

    



admin.site.register(Department, DepartmentAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(MedicalRecord, MedicalRecordAdmin)
admin.site.register(Billing, BillingAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(Drug, DrugAdmin)
admin.site.register(LabTest, LabTestAdmin)
admin.site.register(LabResult, LabResultAdmin)
# admin.site.register(PrescribedMedication, PrescribedMedicationsAdmin)



