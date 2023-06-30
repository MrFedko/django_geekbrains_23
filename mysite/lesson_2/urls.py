from django.urls import path

from lesson_2 import views

urlpatterns = [
    path('', views.index, name="index"),
    path('news/', views.news),
    path('courses_list/', views.courses_list),
]
