from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from tutorhub.models import *
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget

class ListSession(ListView):
    model = Session

class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = ['student_id', 'first_name', 'last_name', 'date', 'building', 'room', 'subject', 'instructor', 'assignment', 'grade', 'apt_time', 'reason_visited', 'visited']
        widgets = {
            'date': AdminDateWidget(attrs={'cols': 80, 'rows': 20}),
        }

class CreateSession(CreateView):
    model = Session
    fields = ['student_id', 'first_name', 'last_name', 'date', 'building', 'room', 'subject', 'instructor', 'assignment', 'grade', 'apt_time', 'reason_visited', 'visited', 'completion']
    success_url = '/'

class ListTutor(ListView):
    model = Tutor

class TutorForm(ModelForm):
    class Meta:
        model = Tutor
        fields = ['user', 'tutor_email', 'first_name', 'last_name', 'phone', 'picture']

class CreateTutor(CreateView):
    model = Tutor
    fields = ['user', 'tutor_email', 'first_name', 'last_name', 'phone', 'picture']
    success_url = '/'

class ListStudent(ListView):
    model = Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'student_id', 'student_email', 'first_name', 'last_name', 'phone', 'grade', 'instructor']

class CreateStudent(CreateView):
    model = Student
    fields = ['user', 'student_id', 'student_email', 'first_name', 'last_name', 'phone', 'grade', 'instructor']
    success_url = '/'

class ListInstructor(ListView):
    model = Instructor

class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        fields = ['user', 'instructor_email', 'first_name', 'last_name', 'phone', 'classes', 'building', 'room']

class CreateInstructor(CreateView):
    model = Instructor
    fields = ['user', 'instructor_email', 'first_name', 'last_name', 'phone', 'classes', 'building', 'room']
    success_url = '/'

class ReflectionForm(ModelForm):
    class Meta:
        model = Reflection
        fields = ['session', 'student', 'tutor', 'instructor', 'reflection']

class CreateReflection(CreateView):
    model = Reflection
    fields = ['session', 'student', 'tutor', 'instructor', 'reflection']
    success_url = '/'

# Create your views here.
