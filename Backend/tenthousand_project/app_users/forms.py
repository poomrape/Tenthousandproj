from django.contrib.auth.forms import UserCreationForm
from .models import Expense
from django import forms

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'description', 'date']
        widgets = {
            'date': forms.TextInput(attrs={'type': 'text'}),
        }
