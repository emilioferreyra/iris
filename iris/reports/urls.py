from django.conf.urls import url
from reports.views import members_by_academic_level


urlpatterns = [
    url(r'^member_academic_level/$', members_by_academic_level),
]
