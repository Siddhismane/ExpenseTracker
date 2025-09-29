from django.db import models

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('FOOD', 'Food'),
        ('TRAVEL', 'Travel'),
        ('SHOPPING', 'Shopping'),
        ('BILLS', 'Bills'),
        ('OTHER', 'Other'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.category} - {self.amount} on {self.date}"
