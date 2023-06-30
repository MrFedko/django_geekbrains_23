from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def go_to_template(request, template: str):
    return render(request, f'lesson_2/{template}')


def hello(request):
    return render(request, 'lesson_2/index.html')
