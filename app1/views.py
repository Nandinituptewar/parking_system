
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from .models import Person
from django.views import View
from django.http import HttpResponse
from .forms import PersonForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
import datetime
from dateutil import relativedelta
from rest_framework import viewsets
from .serializers import PersonSerializer

class HomeView(TemplateView):
    model=Person
    template_name = "app1/home.html"

class TableView(TemplateView):
    model = Person
    template_name = "app1/table_dispaly.html"
    context=Person.objects.all()

    #stu={
     #   'st':context
    #}
    def get(self,request,**kwargs):
        return render(request,'app1/table_dispaly.html',{'stu':self.context})


class FormView_1(TemplateView):
    template_name = "app1/form_page.html"
    #form_class=PersonForm

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(**kwargs)
        fm=PersonForm()
        context={'form':fm}
        return context

    def post(self, request):
        fm=PersonForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            sts =fm.cleaned_data['status']
            plt_num =fm.cleaned_data['plate_num']
            reg=Person(name=nm,plate_num=plt_num,status=sts)

            if Person.objects.filter( plate_num=plt_num ).exists():
                messages.success(request, 'Already registered')
                return redirect('form-page')
            else:
                 messages.success(request,'Successfully registered ')
                 reg.save()
                 return redirect('finish-page')

        return redirect('form-page')

class Finish_entry(TemplateView):
    model = Person
    template_name = "app1/finish_form.html"

    def get(self,request):
        data=Person.objects.last()
        return render(request, "app1/finish_form.html", {'data': data})

class parking_finish(TemplateView):
    model=Person
    template_name = "app1/parking_finish.html"

    def post(self,request):
        if request.method == "POST":
            data = request.POST['uniq_id']
            if Person.objects.filter(id=data).exists():
                c=Person.objects.get(id=data)
                start_time=c.time_1
                date_1 = datetime.datetime.now()
                difference = relativedelta.relativedelta(date_1,start_time )
                years = difference.years
                months = difference.months
                days = difference.days
                hours = difference.hours
                minutes = ((difference.minutes)*0.2)
                msg="your Charges are %f" %minutes
                messages.success(request, msg)
            else:
                messages.success(request, 'Entered Id is not acceptable')
            return render(request, "app1/parking_finish.html" )

class forget_password(TemplateView):
    model=Person
    template_name = "app1/forget_id.html"

    def post(self,request):
        if request.method == "POST":
            data = request.POST['uniq_id']
            if Person.objects.filter(plate_num=data).exists():
                c=Person.objects.get(plate_num=data)
                id_person=c.id

                msg="your Id is %d" %id_person
                messages.success(request, msg)
            else:
                messages.success(request, 'Entered Plate number is not acceptable')
            return render(request, "app1/forget_id.html" )


from rest_framework.authentication import TokenAuthentication

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all().order_by('id')
    authentication_classes = (TokenAuthentication,)

