from django.conf.urls import patterns, include, url
from django.contrib import admin
#TemplateView allows plain templates to be rendered
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name="tutorhub/index.html")),
    url(r'^admin/', include(admin.site.urls)),
)
