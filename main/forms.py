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


class UserSignIn(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    # let's it char for the view can auto add comma
    # and then change it back to float when save
    cash = forms.CharField()
    class Meta:
        model = User
        fields = ['username','password','confirm_password','cash']


class UserLogIn(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password']
