from django import forms
from .models import *

class question_form(forms.ModelForm):
    class Meta:
        model=questions_model
        fields=['author','question']
class answer_form(forms.ModelForm):
    class Meta:
        model=answers_model
        fields=['question','answer']
        
