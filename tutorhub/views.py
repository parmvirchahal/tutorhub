from django.shortcuts import render
from django.views.generic.edit import CreateView
from tutorhub.models import *
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget

class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = ['student_id', 'first_name', 'last_name', 'date', 'building', 'room', 'subject', 'instructor', 'assignment', 'grade', 'apt_time', 'reason_visited', 'visited']
        widgets = {
            'date': AdminDateWidget(attrs={'cols': 80, 'rows': 20}),
        }

class CreateSession(CreateView):
    model = Session
    fields = ['student_id', 'first_name', 'last_name', 'date', 'building', 'room', 'subject', 'instructor', 'assignment', 'grade', 'apt_time', 'reason_visited', 'visited']
    success_url = '/'

# Create your views here.
