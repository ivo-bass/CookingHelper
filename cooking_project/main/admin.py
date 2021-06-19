from django.contrib import admin

from cooking_project.main.models import Choice


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['food', 'garnish', 'meal', 'due_date']
