from main.models import *
from django.contrib.auth.models import User
from django import forms


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = '__all__'


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    cash = forms.FloatField()
    class Meta:
        model = User
        fields = ['username','password','cash']
