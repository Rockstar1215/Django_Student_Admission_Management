from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import logout
from .models import Student
from .forms import StudentForm


# Create your views here.
@login_required
def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })

@login_required
def view_student(request, id):
    return HttpResponseRedirect(reverse('index'))

@login_required
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {
        'form': StudentForm()
    })

@login_required
def edit(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True
            })
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {
        'form': form
    })

@login_required
def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect(reverse('index'))
        else:
            messages.error(request, 'Invalid credentials or not an admin user')
    return render(request, 'admin_login.html')


def admin_logout(request):
    logout(request)
    return redirect(reverse('admin_login'))
