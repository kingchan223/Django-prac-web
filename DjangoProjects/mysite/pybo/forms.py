from django import forms
from pybo.models import Question

class QuestionForm(forms.ModelForm):
    class meta:
        model = Question
        fields = ['subject', 'content']