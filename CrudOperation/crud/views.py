from django.shortcuts import render,HttpResponseRedirect
from .forms import EmpForm
from .models import Employee

def index(request):
    if(request.method=='POST'):
        fm = EmpForm(request.POST)
        if fm.is_valid():
            nm =fm.cleaned_data['name']
            em =fm.cleaned_data['email']
            pwd  =fm.cleaned_data['pwd']
            reg = Employee(name=nm,email=em,pwd=pwd)
            reg.save()
            fm = EmpForm()
        
    else:
        fm=EmpForm()
    emp =Employee.objects.all()

    return render(request, 'index.html',{'form':fm,'emp':emp})


def update(request,id):
    if(request.method=='POST'):
        
        emp = Employee.objects.get(pk=id)
        fm = EmpForm(request.POST,instance=emp)
        if(fm.is_valid()):
            fm.save()
    else:
        emp = Employee.objects.get(pk=id)
        fm = EmpForm(instance=emp)

    return render(request,'update.html',{'fm':fm})


def delete(request,id):
    if(request.method=='POST'):
        emp = Employee.objects.get(pk=id)
        emp.delete()
    return HttpResponseRedirect('/')