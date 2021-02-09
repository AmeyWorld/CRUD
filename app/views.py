from django.shortcuts import render,HttpResponseRedirect
from .forms import student_reg
from .models import student_info
from django.contrib import messages
# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = student_reg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = student_info(name=nm, email=em, password=pw)
            reg.save()
            fm = student_reg()
            # messages.add_message(request, messages.SUCCESS,'Data Saved....')
            messages.info(request,'Data Saved....')
            # fm.save()
    else:
        fm = student_reg()
    stud = student_info.objects.all()
    return render(request,'app/addandshow.html' ,{'form':fm, 'stu':stud})

def delete_std(request, id):
    if request.method == 'POST':
        stud = student_info.objects.get(pk=id)
        print('--',stud)
        stud.delete()
        return HttpResponseRedirect('/')

def Update_Record(request, id):
    if request.method == 'POST':
        stud = student_info.objects.get(pk=id)
        print('----1------',stud)
        fm =student_reg(request.POST, instance=stud)
        if fm.is_valid():
            fm.save()
        else:
            stud = student_info.objects.get(pk=id)
            print('----2------', stud)
            fm = student_reg(instance=stud)
    return render(request, 'app/update.html',{'form':fm})

#  def
