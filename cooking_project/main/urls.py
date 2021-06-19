from django.urls import path

from cooking_project.main.views import index

urlpatterns = [
    path('', index, name='index'),
]