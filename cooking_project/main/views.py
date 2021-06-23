from django.shortcuts import render, redirect

from cooking_project.food.models import Food
from cooking_project.main.forms import ChoiceForm
from cooking_project.main.models import Choice

import random


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


def make_random_choice(model):
    items = list(model.objects.all())
    return random.choice(items)


def suggest_random_food(request):
    if request.method == 'GET':
        model = Food
        food = make_random_choice(model)
        context = {'food': food}
        return render(request, 'suggest.html', context)


def test(request):
    return render(request, 'base.html')