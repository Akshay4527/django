from django.shortcuts import render
from app1.models import student
from app1.forms import studentForm
# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello World")
def index(request):
    return render(request,'demo.html')
def list(request):
    k=student.objects.all()
    return render(request,'list.html',{"s":k})
def form1(request):
    form = studentForm()
    if request.method == "POST":
        form =studentForm(request.POST)
        if form.is_valid():
            form.save()
            return list(request)
        else:
            form= studentForm()
    return render(request,"form1.html",{"form":form})
def form2(request):
    if request.method == "POST":
        form =studentForm(request.POST)
        if form.is_valid():
            form.save()
            return list(request)
    return render(request,"form2.html")
def form3(request):
    if request.method == "POST":
        k=request.POST['n']
        p=request.POST['a']
        o=student.objects.create(name=k,age=p)
        o.save()
        return list(request)
    return render(request,'form3.html')