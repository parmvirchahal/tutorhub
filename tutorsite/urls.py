from django.conf.urls import patterns, include, url
from django.contrib import admin
#TemplateView allows plain templates to be rendered
from django.views.generic import TemplateView
from tutorhub.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name="tutorhub/index.html")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create-session/', CreateSession.as_view(template_name="tutorhub/create_form.html")),
    url(r'^list-session/', ListSession.as_view(template_name="tutorhub/sessions_list.html")),
    url(r'^4NuxxSfbo1create-tutor/', CreateTutor.as_view(template_name="tutorhub/tutor_form.html")),
    url(r'^list-tutor/', ListTutor.as_view(template_name="tutorhub/tutor_list.html")),
    url(r'^create-student/', CreateStudent.as_view(template_name="tutorhub/student_form.html")),
    url(r'^list-student/', ListStudent.as_view(template_name="tutorhub/student_list.html")),
    url(r'^NE3zZmVO2Xcreate-instructor/', CreateInstructor.as_view(template_name="tutorhub/instructor_form.html")),
    url(r'^list-instructor', ListInstructor.as_view(template_name="tutorhub/instructor_list.html")),
)
