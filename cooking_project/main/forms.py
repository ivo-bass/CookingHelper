from django import forms

from cooking_project.main.models import Choice


class ChoiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChoiceForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

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
