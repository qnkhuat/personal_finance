from django.urls import path,include
from . import views
app_name='main'
urlpatterns=[
    path('income',views.IncomeInput.as_view(),name='income'),
    path('expense',views.ExpenseInput.as_view(),name='expense'),
    path('signin',views.UserSignIn.as_view(),name='signin')
]
