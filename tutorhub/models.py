from django.db import models
from django.contrib.auth.models import User
# Create your models here.

SESSION_TYPE = (
    ("Tutoring", 'Tutoring Session'),
    ("Workshop", 'Workshop Session'),
    ("Digital", 'Digital Tutoring Session'),
)

APT_TIME = (
    ("B1D1", 'Block 1 Day 1'),
    ("B1D2", 'Block 1 Day 2'),
    ("B2D1", 'Block 2 Day 1'),
    ("B2D2", 'Block 2 Day 2'),
    ("B3D1", 'Block 3 Day 1'),
    ("B3D2", 'Block 3 Day 2'),
    ("B4D1", 'Block 4 Day 1'),
    ("B4D2", 'Block 4 Day 2'),
    ("A", 'A Lunch'),
    ("B", 'B Lunch'),
    ("C", 'C Lunch'),
    ("Eagle Time", 'Eagle Time'),
    ("After School Monday", 'After School Monday'),
    ("After School Thursday", 'After School Thursday'),
)

GRADE = (
    ("9", 'Ninth Grade'),
    ("10", 'Tenth Grade'),
    ("11", 'Eleventh Grade'),
    ("12", 'Twelfth Grade'),
)

CLASS = (
    ("English", 'English'),
    ("Social Studies", 'Social Studies'),
    ("Science", 'Science'),
    ("Mathematics", 'Mathematics'),
    ("Fine Arts", 'Fine Arts (Art, Music, Theatre)'),
    ("Business", 'Business/Marketing'),
    ("IB", 'IB/TOK'),
    ("AVID", 'AVID'),
    ("PE", 'PE/Health/Driver\'s Education'),
    ("JROTC", 'JROTC'),
    ("SAT", 'SAT Prep/ACT Prep/ Test Prep'),
    ("ESOL", 'ESOL'),
    ("World Languages", 'World Langauges'),
    ("Other", 'Independent/Other'),
)

VISITED = (
    ("Never", 'I have never been to the EWC before.'),
    ("Not this school year", 'Yes, but not this school year.'),
    ("Already been this school year", 'Yes, I have already been here this school year.'),
)

REASON_VISITED = (
    ("Teacher required", 'It was teacher required.'),
    ("Teacher offered extra credit", 'My teacher offered extra credit.'),
    ("Been before and found it useful", 'I have been here before and found it useful.'),
    ("Heard about it and wanted to try", 'I heard about it and wanted to give it a try.'),
    ("Rewriting and resubmitting essay", 'I am rewriting and resubmitting an essay.'),
)

class Tutor(models.Model):
    user = models.OneToOneField(User)
    tutor_email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)
    picture = models.ImageField(upload_to='images/%Y/%m/%d')
    
    def __str__(self):
        return self.first_name + " " + self.last_name

class Student(models.Model):
    user = models.OneToOneField(User)
    student_id = models.CharField(max_length=35)
    student_email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)
    grade = models.CharField(max_length=2, choices=GRADE)
    email = models.CharField(max_length=100)
    instructor = models.CharField(max_length=35)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Instructor(models.Model):
    user = models.OneToOneField(User)
    instructor_email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)
    classes = models.CharField(max_length=25, choices=CLASS)
    building = models.CharField(max_length=25)
    room = models.CharField(max_length=25)

    def __str__(self):
        return self.last_name

class Session(models.Model):
    student_id = models.CharField(max_length=35)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    date = models.DateField()
    building = models.CharField(max_length=25)
    room = models.CharField(max_length=4)
    subject = models.CharField(max_length=25, choices=CLASS)
    instrutor = models.CharField(max_length=25)
    assignment = models.CharField(max_length=100)
    grade = models.CharField(max_length=2, choices=GRADE)  
    apt_time = models.CharField(max_length=25, choices=APT_TIME)
    reason_visited = models.CharField(max_length=50, choices=REASON_VISITED)
    visited = models.CharField(max_length=50, choices=VISITED)

class Expertise(models.Model):
    tutor_email = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Expertise"

class Availability(models.Model):
    tutor_email = models.CharField(max_length=100)
    date = models.DateField()

    class Meta:
        verbose_name_plural = "Availabilities"

class Email_Authentication(models.Model):
    tutor_email = models.CharField(max_length=100)
