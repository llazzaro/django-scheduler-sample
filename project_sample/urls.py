from django.views.generic import TemplateView
from django.conf.urls import include, url

from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="homepage.html"),),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^fullcalendar/', TemplateView.as_view(template_name="fullcalendar.html"), name='fullcalendar'),
    url(r'^admin/', admin.site.urls),
]
