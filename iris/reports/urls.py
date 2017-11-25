from django.conf.urls import url
from reports.views import members_by_academic_level
from reports.views import members_by_location
from reports.views import mothers_quantity
from reports.views import index


urlpatterns = [
    url(
        r'^$',
        index,
        name="reports_home"
    ),
    url(
        r'^members_academic_level/$',
        members_by_academic_level,
        name="academic_level_report"
    ),
    url(
        r'^members_location/$',
        members_by_location,
        name="location_report"
    ),
    url(
        r'^mothers/$',
        mothers_quantity,
        name="mothers_report"
    ),
]
