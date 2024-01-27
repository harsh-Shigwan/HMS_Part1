from django.contrib import admin
from patient_dashboard.models.models import Patient
# Register your models here.
# admin.py



class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone_number', 'health_records')

admin.site.register(Patient, PatientAdmin)