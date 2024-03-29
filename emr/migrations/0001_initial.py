# Generated by Django 5.0.1 on 2024-02-08 09:55

import django.db.models.deletion
import encrypted_model_fields.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', encrypted_model_fields.fields.EncryptedCharField()),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', encrypted_model_fields.fields.EncryptedCharField()),
                ('price', encrypted_model_fields.fields.EncryptedCharField()),
                ('quantity', encrypted_model_fields.fields.EncryptedCharField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', encrypted_model_fields.fields.EncryptedCharField()),
                ('last_name', encrypted_model_fields.fields.EncryptedCharField()),
                ('phone_number', encrypted_model_fields.fields.EncryptedCharField()),
                ('dob', encrypted_model_fields.fields.EncryptedCharField()),
                ('next_of_kin', encrypted_model_fields.fields.EncryptedCharField()),
                ('address_of_kin', encrypted_model_fields.fields.EncryptedTextField()),
                ('place_of_origin', encrypted_model_fields.fields.EncryptedCharField()),
                ('mswd', encrypted_model_fields.fields.EncryptedCharField(blank=True, null=True)),
                ('xray_number', encrypted_model_fields.fields.EncryptedCharField(blank=True, null=True)),
                ('ethnic_group', encrypted_model_fields.fields.EncryptedCharField(blank=True, null=True)),
                ('occupation', encrypted_model_fields.fields.EncryptedCharField(blank=True, null=True)),
                ('religion', encrypted_model_fields.fields.EncryptedCharField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', encrypted_model_fields.fields.EncryptedCharField()),
                ('last_name', encrypted_model_fields.fields.EncryptedCharField()),
                ('email', models.CharField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('doctor_type', encrypted_model_fields.fields.EncryptedCharField()),
                ('doctor_specialization', encrypted_model_fields.fields.EncryptedCharField()),
                ('is_superadmin', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='emr.department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', encrypted_model_fields.fields.EncryptedCharField()),
                ('description', encrypted_model_fields.fields.EncryptedTextField()),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='emr.patient')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', encrypted_model_fields.fields.EncryptedCharField()),
                ('genotype', encrypted_model_fields.fields.EncryptedCharField()),
                ('diagnoses', encrypted_model_fields.fields.EncryptedTextField()),
                ('admitted_at', models.DateTimeField(auto_now_add=True)),
                ('discharged_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='emr.patient')),
            ],
        ),
        migrations.CreateModel(
            name='LabResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', encrypted_model_fields.fields.EncryptedTextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='emr.labtest')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='emr.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', encrypted_model_fields.fields.EncryptedCharField()),
                ('description', encrypted_model_fields.fields.EncryptedCharField()),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='emr.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_appointments', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='emr.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vital_signs', encrypted_model_fields.fields.EncryptedTextField(blank=True, null=True)),
                ('complaint', encrypted_model_fields.fields.EncryptedTextField(blank=True, null=True)),
                ('diagnosis', encrypted_model_fields.fields.EncryptedTextField(blank=True, null=True)),
                ('examination', encrypted_model_fields.fields.EncryptedTextField(blank=True, null=True)),
                ('plan', encrypted_model_fields.fields.EncryptedTextField(blank=True, null=True)),
                ('medication_details', models.JSONField()),
                ('others', encrypted_model_fields.fields.EncryptedTextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='emr.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PrescribedMedication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vital_signs', encrypted_model_fields.fields.EncryptedTextField(blank=True, null=True)),
                ('complaint', encrypted_model_fields.fields.EncryptedTextField(blank=True, null=True)),
                ('diagnosis', encrypted_model_fields.fields.EncryptedTextField(blank=True, null=True)),
                ('examination', encrypted_model_fields.fields.EncryptedTextField(blank=True, null=True)),
                ('plan', encrypted_model_fields.fields.EncryptedTextField(blank=True, null=True)),
                ('dosage', encrypted_model_fields.fields.EncryptedCharField(blank=True, null=True)),
                ('frequency', encrypted_model_fields.fields.EncryptedCharField(blank=True, null=True)),
                ('duration', encrypted_model_fields.fields.EncryptedCharField(blank=True, null=True)),
                ('others', encrypted_model_fields.fields.EncryptedTextField(blank=True, null=True)),
                ('drug', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='emr.drug')),
                ('prescription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prescribed_medications', to='emr.prescription')),
            ],
        ),
    ]
