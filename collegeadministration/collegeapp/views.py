from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import StudentForm
from .models import Student


# Create your views here.
def index(request):
    student = Student.objects.all()
    context = {
        'student_details': student
    }
    return render(request, 'index.html', context=context)


def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'detail.html', {'student': student})


def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        image = request.FILES['profilepic']

        student = Student(name_student=name, address=address, dob=dob, propic=image)
        student.save()
    return render(request, 'add.html')


def update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, request.FILES, instance=student)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'student': student})


def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(id=id)
        student.delete()
        return redirect('/')
    return render(request, 'delete.html')
