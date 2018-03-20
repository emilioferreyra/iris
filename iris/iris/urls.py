"""iris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
# The next 2 modules are necessary to redirect root to admin site
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib import admin


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from .site import DashboardSite
from .views import home

admin.site = DashboardSite()
admin.sites.site = admin.site
admin.autodiscover()

urlpatterns = [
    # The next url redirect root to admin site
    url(r'^$', RedirectView.as_view(
        url=reverse_lazy('admin:index'),
        permanent=False)
        ),
    url(r'^$', home, name='home'),
    url(
        r'^about/$',
        TemplateView.as_view(template_name="about.html"),
        name='about'
    ),
    url(
        r'^contact/$',
        TemplateView.as_view(template_name="contact.html"),
        name='contact'
    ),
    url(
        r'^services/$',
        TemplateView.as_view(template_name="services.html"),
        name='services'
    ),
    url(r'^reports/', include('reports.urls')),
    url(r'^report_builder/', include('report_builder.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }),
    url(r'^_nested_admin/', include('nested_admin.urls')),
]

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT
#     )
