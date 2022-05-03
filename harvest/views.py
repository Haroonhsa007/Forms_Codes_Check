from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Person
from .forms import PersonForm


def home(request):
    return render(request, 'harvest/home.html')


def about(request):
    return render(request, 'harvest/about.html')


def people(request):
    context = {'people': Person.objects.all()}
    return render(request, 'harvest/people.html', context)


def add_person(request):
    submitted = False
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_person?submitted=True')
    else:
        form = PersonForm
        if 'submitted' in request.GET:
            submitted = True

    context = {'form': form, 'submitted': submitted}
    return render(request, 'harvest/add_person.html', context)


def edit_person(request, person_id):
    person = Person.objects.get(pk=person_id)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('harvest-people')
    context = {'person': person,
               'form': form}
    return render(request, 'harvest/edit_person.html', context)


def search_people(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        people = Person.objects.filter(id__contains=searched)
        context = {'people': people}
        if searched == '':
            messages.warning(request, 'Empty search')
    else:
        context = {}

    return render(request, 'harvest/people.html', context)
