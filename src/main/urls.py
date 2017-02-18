from django.conf.urls import url
from django.views.generic import TemplateView

from .views import contact 
urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="home.html")),
	url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    url(r'^contact/$', contact, name='contact'),
    ]