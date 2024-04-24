from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
# Create your views here.

def create(request):
    if request.method == "POST":
        nm = request.POST["ename"]
        sal = request.POST["esalary"]
        pos = request.POST["eposition"]
        bgrp = request.POST["ebloodgroup"]
        ag = request.POST["eage"]
        
        #print(nm,sal,pos,bgrp,ag)
        emp = Employee.objects.create(name=nm,salary=sal,position=pos,blood_g=bgrp,age=ag)
    
        emp.save()
        return redirect("/s")

    else:
        return render(request,"create.html")

def show(request):
    emp=Employee.objects.all()

    context={}
    context["employee"]=emp


    return render(request,"table.html",context)

def delete(request,rid):
    emp=Employee.objects.filter(id=rid)

    emp.delete()
    return redirect("/s")

def update(request,pid):
    if request.method == 'GET':
        em=Employee.objects.filter(id=pid)

        context={}
        context['data']=em

        return render(request,"edited.html",context)

    else:
        nm = request.POST["ename"]
        sal = request.POST["esalary"]
        pos = request.POST["eposition"]
        bg = request.POST["ebloodgroup"]
        ag = request.POST["eage"]

        m =Employee.objects.filter(id=pid)
        m.update(name=nm,salary=sal,position=pos,blood_g=bg,age=ag)

        return redirect("/s")