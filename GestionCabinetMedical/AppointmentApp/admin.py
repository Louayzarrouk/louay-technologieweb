from django.contrib import admin

# Register your models here.
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_date', 'doctor', 'patient', 'status', 'duration_minutes')
    list_filter = ('status', 'doctor', 'appointment_date')
    search_fields = ('doctor_last_name', 'patientlast_name', 'patient_national_id', 'reason')
    ordering = ('appointment_date',)