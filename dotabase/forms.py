from django import forms
from .models import WeeklyPolls

class WeeklyPollsForm(forms.ModelForm):

    class Meta:
        model = WeeklyPolls
        fields = ('answer',)