from django.shortcuts import render , redirect
from django.views import generic
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# my files
from .forms import *


@login_required
def index(request):
    return render(request,'main/dashboard.html')

class CashInAndOutInput(LoginRequiredMixin,generic.View):
    template_name = 'main/income.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            money    = form.save(commit = False)
            _member = request.user.member
            _type   = form.cleaned_data['type']
            _amount = form.cleaned_data['amount']
            _notes  = form.cleaned_data['notes']

            money.user = request.user.member
            money.type=_type
            money.amount=_amount
            money.notes=_notes
            money.save()

            self.update(_member,_type,_amount)



        else:
            messages.warning(request, 'Something went wrong')
        return render(request, self.template_name,{'form':form})



class ExpenseInput(CashInAndOutInput):
    form_class  = ExpenseForm
    def update(self,_member,_type,_amount):
        _member.cash -= _amount
        _member.save()


class IncomeInput(CashInAndOutInput):
    form_class  = IncomeForm
    def update(self,_member,_type,_amount):
        if _type in ['f','o']: #fixed income or other
            _member.cash += _amount
            _member.save()

        if _type=='i': # interests
            # TODO: need to automate this by if this type auto list the list of interest
            _member.cash += _amount
            _member.save()

        if _type =='b': # borrow
            # TODO: need to subtract in the total asset
            _member.cash += _amount
            _member.save()


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

            #check password
            if password != confirm_password:
                messages.warning(request, 'Confirm password not match')
                return render(request,self.template_name,{'form':form,'site':'signin'})

            user.set_password(password)

            user.save()

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
