from django.db import models

class Expense(models.Model):
    CATEGORIES = [
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('health', 'Health'),
        ('entertainment', 'Entertainment'),
        ('others', 'Others')
    ]

    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    date = models.DateField()
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - R$ {self.amount}"

# Create your models here.
