from main.models import *
from django import forms


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = '__all__'
