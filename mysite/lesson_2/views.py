from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'lesson_2/index.html')


def news(request):
    return render(request, 'lesson_2/news.html')


def courses_list(request):
    return render(request, 'lesson_2/courses_list.html')
