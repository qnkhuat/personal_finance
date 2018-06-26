from django.urls import path,include
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import views as authViews
from . import views
app_name='main'
urlpatterns=[
    path('income',login_required(views.IncomeInput.as_view()),name='income'),
    path('expense',login_required(views.ExpenseInput.as_view()),name='expense'),
    path('signin',views.UserSignIn.as_view(),name='signin'),
]



### override django auth path
urlpatterns +=[
    path('login/', authViews.LoginView.as_view(), name='login'),
    path('logout/', authViews.LogoutView.as_view(next_page='/'), name='logout'),
    path('password_change/', authViews.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', authViews.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', authViews.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
