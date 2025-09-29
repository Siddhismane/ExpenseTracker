from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_expense, name='add_expense'),
    path('', views.list_expenses, name='list_expenses'),
    path('edit/<int:pk>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete_expense'),
    path('dashboard/', views.dashboard, name='dashboard'),


]
