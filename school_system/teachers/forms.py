from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'email', 'phone', 'address', 'hire_date']
        widgets = {
            'hire_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        }
