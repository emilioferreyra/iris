from django.contrib.admin.sites import AdminSite
from django.conf.urls import url

from .views import HomeView
from .views import NestView1
from .views import NestView2


class DashboardSite(AdminSite):
    def get_urls(self):
        urls = super(DashboardSite, self).get_urls()
        custom_urls = [
            url(r'^$', self.admin_view(HomeView.as_view()), name='index'),
            url(r'nest1/^$', self.admin_view(NestView1.as_view()), name='nest1'),
            url(r'nest1/nest2/^$', self.admin_view(NestView2.as_view()), name='nest2'),
        ]

        # del urls[0]
        return custom_urls + urls
