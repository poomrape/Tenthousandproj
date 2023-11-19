from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from app_users.forms import RegisterForm
from django.contrib.auth import login
from django.urls import reverse
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request: HttpRequest):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
    else:
        form = RegisterForm()

    context = {"form": form}
    return render(request, "app_users/register.html", context)

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    total_amount = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    total_amount = 10000-total_amount
    return render(request, 'expense_list.html', {'expenses': expenses,'total_amount': total_amount})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

@login_required
def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    expense.delete()
    return redirect('expense_list')




