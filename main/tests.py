from django.test import TestCase
from .models import *
from django.contrib.auth.models import User


class Income_Test(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        Member.objects.create(user=user,cash=10000)

        member = Member.objects.first()
        income= Income.objects.create(user=member,type='f',amount=1000,notes='this is a test')

    def test_check(self):
        income = Income.objects.first()
        self.assertIsInstance(income.amount,float)


class Expense_Test(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        Member.objects.create(user=user,cash=10000)

        member = Member.objects.first()
        expense= Expense.objects.create(user=member,type='f',amount=1000,notes='this is a test')

    def test_check(self):
        expense = Expense.objects.first()
        self.assertIsInstance(expense.amount,float)
