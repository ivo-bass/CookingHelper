from django.urls import path

from cooking_project.main.views import index, test, suggest_random_food

urlpatterns = [
    path('', index, name='index'),
    path('test/', test, name='test'),
    path('suggest', suggest_random_food, name='suggest'),
]