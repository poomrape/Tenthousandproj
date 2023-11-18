from django.urls import path, include
from . import views
urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('register', view=views.register, name='register'),
    path('list/', views.expense_list, name='expense_list'),
    path('add/', views.add_expense, name='add_expense'),
    path('delete_expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]