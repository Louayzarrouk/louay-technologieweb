from django.contrib import admin
from .models import User, Doctor, Patient,Specialty


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','license_number','phone')
    search_fields = ('specialties',)
    ordering = ('last_name',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','phone')
    search_fields = ('last_name','first_name','national_id')
    ordering = ('last_name',)



# Register your models here.
