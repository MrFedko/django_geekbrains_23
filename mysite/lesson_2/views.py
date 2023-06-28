from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def check_kwargs(request, **kwargs):
    return HttpResponse(f"kwargs: {kwargs}")


def hello(request):
    return render(request, 'lesson_2/index.html')
