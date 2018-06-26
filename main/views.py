from django.shortcuts import render , redirect
from django.views import generic
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# my files
from .forms import *
from .worker import *


class IncomeInput(LoginRequiredMixin,generic.View):
    form_class  = IncomeForm
    template_name = 'main/income.html'
    # redirect_field_name = 'main:login'
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            customer = form.save(commit = False)
            user     = form.cleaned_data['user']
            type     = form.cleaned_data['type']
            amount   = form.cleaned_data['amount']
            notes    = form.cleaned_data['notes']
            updateIncome(user,type,amount)
            customer.save()
        else:
            messages.warning(request, 'Something went wrong')
        return render(request, self.template_name,{'form':form})


class ExpenseInput(LoginRequiredMixin,generic.View):
    form_class  = ExpenseForm
    template_name = 'main/income.html'
    redirect_field_name = 'redirect_to'

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            customer = form.save(commit = False)
            user     = form.cleaned_data['user']
            type     = form.cleaned_data['type']
            amount   = form.cleaned_data['amount']
            notes    = form.cleaned_data['notes']
            updateExpense(user,type,amount)
            customer.save()
        else:
            messages.warning(request, 'Something went wrong')
        return render(request, self.template_name,{'form':form})


class UserSignIn(generic.View):
    form_class = UserSignIn
    template_name = 'main/sign_in.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form,'site':'signin'})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username         = form.cleaned_data['username']
            password         = form.cleaned_data['password']
            cash             = float(form.cleaned_data['cash'].replace(',',''))
            confirm_password = form.cleaned_data["confirm_password"]
            print('cash',cash)

            #check password
            if password != confirm_password:
                messages.warning(request, 'Confirm password not match')
                return render(request,self.template_name,{'form':form,'site':'signin'})

            user.set_password(password)
            user.save()
            #create user first then create member
            user.refresh_from_db()  # load the profile instance created by the signal
            user.member.cash = cash
            user.save()

            #login user objects if succeed
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('main:income')
        # print(form)
        messages.warning(request, 'User name existed or not valid')
        return render(request,self.template_name,{'form':form,'site':'signin'})



def anchor():
    pass
