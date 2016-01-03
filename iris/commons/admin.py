from django.contrib import admin
from .models import DocumentType, PhoneType, AcademicLevel


admin.site.register(DocumentType)
admin.site.register(PhoneType)
admin.site.register(AcademicLevel)
