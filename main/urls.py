from django.urls import path,include
from . import views

urlpatterns=[
    path('income',views.IncomeForm.as_view(),name='income')
]
