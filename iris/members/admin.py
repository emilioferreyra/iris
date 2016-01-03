from django.contrib import admin
from .models import Disability, Cane, MaritalStatus, PropertyType, Member, \
Kinship, Kinsman, HousePart, HouseMaterial, Housing, MemberAddress


admin.site.register(Disability)
admin.site.register(Cane)
admin.site.register(MaritalStatus)
admin.site.register(PropertyType)
admin.site.register(Member)
admin.site.register(Kinship)
admin.site.register(Kinsman)
admin.site.register(HousePart)
admin.site.register(HouseMaterial)
admin.site.register(Housing)
admin.site.register(MemberAddress)
