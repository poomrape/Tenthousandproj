from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.date}"
    
    def get_absolute_url(self):
        return reverse('expense_list')