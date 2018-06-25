from django.shortcuts import render
from .forms import *
from django.views import generic


class IncomeForm(generic.View):
    form_class  = IncomeForm
    template_name = 'main/income.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            customer = form.save(commit = False)
            user     = form.cleaned_data['user_now']
            type     = form.cleaned_data['type']
            amount   = form.cleaned_data['amount']
            notes    = form.cleaned_data['notes']
            customer.user_now.cash = form.cleaned_data['amount']
            customer.user_now.save()
            customer.save()
        else:
            print('not valid')
        return render(request, self.template_name,{'form':form})
