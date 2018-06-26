from django.shortcuts import render , redirect
from django.views import generic
from django.contrib.auth import authenticate,login

# my files
from .forms import *
from .worker import *

class IncomeInput(generic.View):
    form_class  = IncomeForm
    template_name = 'main/income.html'

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
            print('not valid')
        return render(request, self.template_name,{'form':form})


class ExpenseInput(generic.View):
    form_class  = ExpenseForm
    template_name = 'main/income.html'

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
            print('not valid')
        return render(request, self.template_name,{'form':form})


class UserSignIn(generic.View):
    form_class = UserForm
    template_name = 'main/login.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            cash     = form.cleaned_data['cash']
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
        return render(request,self.template_name,{'form':form})








def anchor():
    pass
