from django import forms
from django_ace import AceWidget
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        widgets = {
            "text": AceWidget(mode='pgsql', theme='dark'),
        }
        exclude = ()