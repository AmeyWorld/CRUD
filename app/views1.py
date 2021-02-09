from django.shortcuts import render,HttpResponseRedirect
from .forms import student_reg
from .models import student_info
from django.contrib import messages

from django.views.generic.base import TemplateView, RedirectView
from django.views import View

class UserAddShowView(TemplateView):
    template_name = 'app/addandshow.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = student_reg()
        stud = student_info.objects.all()
        context = {'form':fm, 'stu':stud}
        return context

    def post(self,request):
        fm = student_reg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = student_info(name=nm, email=em, password=pw)
            reg.save()
            fm = student_reg()
            # messages.add_message(request, messages.SUCCESS,'Data Saved....')
            messages.info(request, 'Data Saved....')
        return HttpResponseRedirect('/')

class UserDelete_View(RedirectView):
   url = '/'
   def get_redirect_url(self, *args, **kwargs):
       del_id = kwargs['id']
       student_info.objects.get(pk=del_id).delete()
       return super().get_redirect_url(*args, **kwargs)


class Update_Record(View):
    def get(self,request, id):
        stud = student_info.objects.get(pk=id)
        fm1 = student_reg(instance=stud)
        return render(request, 'app/update.html', {'form': fm1})

    def post(self,request, id):
        print(request.method)
        stud = student_info.objects.get(pk=id)
        fm = student_reg(request.POST, instance=stud)
        if fm.is_valid():
            fm.save()
        return render(request, 'app/update.html', {'form': fm})