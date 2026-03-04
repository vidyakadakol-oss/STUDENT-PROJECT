from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

from .models import Student, Course
from .forms import StudentForm, CourseForm


# =========================
# STUDENT LIST
# =========================
def student_list(request):
    students = Student.objects.all().order_by('name')

    # Filtering
    course_id = request.GET.get('course')
    if course_id:
        students = students.filter(course_id=course_id)

    # Pagination (10 per page)
    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    courses = Course.objects.all()

    return render(request, 'students/list.html', {
        'page_obj': page_obj,
        'courses': courses
    })


# =========================
# ADD STUDENT
# =========================
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'students/add.html', {'form': form})


# =========================
# EDIT STUDENT
# =========================
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/edit.html', {'form': form})


# =========================
# DELETE STUDENT
# =========================
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')


# =========================
# STUDENT DETAIL
# =========================
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)

    return render(request, 'students/detail.html', {
        'student': student
    })


# =========================
# COURSE LIST (CBV)
# =========================
class CourseListView(ListView):
    model = Course
    template_name = 'courses/list.html'
    context_object_name = 'courses'


# =========================
# COURSE DETAIL (CBV)
# =========================
class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'


# =========================
# ADD COURSE
# =========================
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()

    return render(request, 'courses/add.html', {'form': form})