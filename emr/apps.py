from django.apps import AppConfig
# from django.db.models.signals import post_save
# from django.dispatch import receiver



class EmrConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emr'
    
    # def ready(self):
    #     from . import signals
        # from .models import PrescribedMedication, Prescription  # Import models here
