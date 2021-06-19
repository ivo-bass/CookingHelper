from django.shortcuts import render, redirect

from cooking_project.main.forms import ChoiceForm
from cooking_project.main.models import Choice


def index(request):
    form = ChoiceForm()
    choices = Choice.objects.all()
    if request.method == 'GET':
        context = {
            'form': form,
            'choices': choices,
        }
        return render(request, 'index.html', context)
    else:
        form = ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
        context = {
            'form': form,
            'choices': choices,
        }
        return render(request, 'index.html', context)
