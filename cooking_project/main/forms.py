from django import forms

from cooking_project.main.models import Choice


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'
        widgets = {
            'due_date': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            ),
        }
