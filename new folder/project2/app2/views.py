from django.shortcuts import render
from app2.models import employee
# Create your views here.
from django.http import HttpResponse
from app2.forms import CustomUserForm,employeeForm
from django.contrib.auth import authenticate,login,logout
def home(request):
    return render(request,'home.html')

def base(request):
    return render(request,'base.html')

def signup_1(request):
    form=CustomUserForm()
    if(request.method=='POST'):
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'signup_1.html',{"form":form})

def login_1(request):
    if(request.method=="POST"):
        name=request.POST['n']
        password=request.POST['p']
        user=authenticate(username=name,password=password)
        if user:
            login(request,user)
            return home(request)
        else:
            return HttpResponse('invalid... no user found')
    return render(request,'login_1.html')
def user_logout(request):
    logout(request)
    return login_1(request)

def add_data(request):
    if(request.method=="POST"):
        name1=request.POST['email']
        name2=request.POST['emp_id']
        name3=request.POST['company']
        name4=request.POST['desigination']
        name5=request.POST['place']
        name6=request.POST['salary']
        dattaa=employee.objects.create(email=name1,emp_id=name2,company=name3,desigination=name4,place=name5,salary=name6)
        dattaa.save()
        return home(request)
    return render(request,'add_data.html')
def view_data(request):
    k=employee.objects.all()
    return render(request,'view_data.html',{"s":k})
def view_item(request,p):
    b=employee.objects.get(pk=p)
    return render(request,'view_item.html',{'b':b})
def edit_item(request,p):
    b=employee.objects.get(pk=p)
    form=employeeForm(instance=b)
    if(request.method=='POST'):
        form=employeeForm(request.POST,instance=b)
        if form.is_valid():
            form.save()
            return view_data(request)
    return render(request,'edit.html',{'form':form})
def delete_item(request,p):
    b=employee.objects.get(pk=p)
    b.delete()
    return view_data(request)