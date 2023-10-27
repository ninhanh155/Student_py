from django.shortcuts import render , redirect , get_object_or_404
from .models import *
from .form import *
from django.contrib.auth import login as qldangnhap
from django.contrib.auth.decorators import login_required
# Create your views here.

def list_student(req):
    students = Student.objects.all()
    return render(req,'home.html',locals())
    
@login_required
def add_student(req):
    if req.method == 'POST':
        form = StudentForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(req,'add_student.html',locals())

@login_required        
def edit_student(req,id):
    cd = get_object_or_404(Student,id = id)
    if req.method == 'POST':
        form = StudentForm(req.POST, instance=cd)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(req,'edit_student.html',locals())

@login_required
def delete_student(req, id):
    cd = get_object_or_404(Student , id = id)
    if req.method == 'POST':
        cd.delete()
        return redirect('home')
    else :
        cd.delete()
    return redirect('home')

def search_student(req):
    if req.method == 'POST':
        search = req.POST['search']
        key = Student.objects.filter(name__contains = search)
    return render(req,'search.html',locals())

def dangky(req):
    if req.method == 'POST' :
        ucf = Bieumau_dangky_thanhvien(req.POST)
        if ucf.is_valid():
            user = ucf.save()
            qldangnhap(req, user)

            return redirect('home')
    else:
        ucf = Bieumau_dangky_thanhvien()

    return render(req, 'register.html', {'form': ucf})