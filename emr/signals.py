# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import PrescribedMedication, Prescription

# @receiver(post_save, sender=PrescribedMedication)
# def create_prescription(sender, instance, created, **kwargs):
#     if created and not instance.prescription:
#         prescription = Prescription.objects.create()
#         instance.prescription = prescription
#         instance.save()