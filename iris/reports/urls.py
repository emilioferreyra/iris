from django.conf.urls import url
from reports.views import members_by_academic_level
from reports.views import members_by_location
from reports.views import mothers_quantity


urlpatterns = [
    url(r'^member_academic_level/$', members_by_academic_level),
    url(r'^members_location/$', members_by_location),
    url(r'^mothers_quantity/$', mothers_quantity),
]
