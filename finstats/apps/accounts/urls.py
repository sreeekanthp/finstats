from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from views import TestView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html")),
)