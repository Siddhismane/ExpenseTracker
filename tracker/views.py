from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from datetime import datetime

import matplotlib
matplotlib.use('Agg')


# Add Expense
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_expenses')
    else:
        form = ExpenseForm()
    return render(request, 'tracker/add_expense.html', {'form': form})

# List Expenses
def list_expenses(request):
    expenses = Expense.objects.all().order_by('-date')
    return render(request, 'tracker/list_expenses.html', {'expenses': expenses})


#edit
def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('list_expenses')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'tracker/add_expense.html', {'form': form})


#delete
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        expense.delete()
        return redirect('list_expenses')
    return render(request, 'tracker/delete_expense.html', {'expense': expense})

from django.db.models import Sum
from datetime import datetime
import io, urllib, base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from .models import Expense
from django.shortcuts import render

def dashboard(request):
    now = datetime.now()
    expenses = Expense.objects.filter(date__year=now.year, date__month=now.month)
    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    count = expenses.count()
    average = round(total / count, 2) if count > 0 else 0  # Calculate average safely

    # Pie chart and category analysis
    data = expenses.values('category').annotate(total=Sum('amount'))
    labels = [d['category'] for d in data]
    sizes = [float(d['total']) for d in data]

    # Analysis table data
    analysis = []
    for d in data:
        percentage = (d['total'] / total * 100) if total > 0 else 0
        analysis.append({'category': d['category'], 'total': d['total'], 'percentage': round(percentage, 1)})

    # Generate pie chart
    chart = None
    if labels and sizes:
        plt.figure(figsize=(4,4))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title("Expenses by Category")
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        chart = urllib.parse.quote(string)
        plt.close()

    return render(request, 'tracker/dashboard.html', {
        'total': total,
        'expenses': expenses,
        'average': average,  # Pass average here
        'chart': chart,
        'analysis': analysis
    })
