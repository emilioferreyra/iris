from django.contrib import admin
from .models import DocumentType, PhoneType, Phone, AcademicLevel


admin.site.register(DocumentType)
admin.site.register(PhoneType)
admin.site.register(Phone)
admin.site.register(AcademicLevel)
