from django.db import models

""" This option is not necessary in this moment, but i think i can use this in the future:

class ExpenseType(models.Model):
    name = models.CharField(max_length=100)
    default_value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
"""
class DefaultExpense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

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
    from_template = models.ForeignKey(DefaultExpense, null=True, blank=True, on_delete=models.SET_NULL) #This is not the way i picture it, but i did in this way for tests, it will be a checkbox.
    date = models.DateField()
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - R$ {self.amount}"






# Create your models here.
