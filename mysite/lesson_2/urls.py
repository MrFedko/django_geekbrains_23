from django.urls import path

from lesson_2.views import check_kwargs, hello

urlpatterns = [
    path('', hello),
    path('<str:word>', check_kwargs)
]
