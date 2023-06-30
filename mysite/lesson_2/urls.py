from django.urls import path

from lesson_2.views import go_to_template, hello

urlpatterns = [
    path('', hello),
    path('<str:template>', go_to_template)
]
