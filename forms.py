from django import forms
from .models import Student, Course


# =========================
# STUDENT FORM
# =========================
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


# =========================
# COURSE FORM
# =========================
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'