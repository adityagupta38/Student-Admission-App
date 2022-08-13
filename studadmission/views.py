from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from studadmission.models import StudAdmission
# Create your views here.


def homepage(request):
    return render(request, 'home.html')


class AddStudent(CreateView):
    model = StudAdmission
    fields = '__all__'
    success_url = '/studlist'


class UpdateStudent(UpdateView):
    model = StudAdmission
    fields = '__all__'
    success_url = '/studlist'


class DelStudent(DeleteView):
    model = StudAdmission
    success_url = '/studlist'


class StudList(ListView):
    model = StudAdmission


class StudDetail(DetailView):
    model = StudAdmission


def stud_admitted(request):
    stud_list = StudAdmission.objects.all()
    return render(request,'students_admitted.html', {'students': stud_list})