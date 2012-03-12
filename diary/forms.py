from django import forms
from diary.models import Greeting

class CreateGreetingForm(forms.ModelForm):
    class Meta:
        model = Greeting
        exclude = ['author', 'date']