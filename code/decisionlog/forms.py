from django import forms

from .models import DecisionLogEntry

class DecisionLogEntryForm(forms.ModelForm):
    class Meta:
        model = DecisionLogEntry
        fields = ("content",)
