from django.db import models

class IncomeType(models.Model):
    name = models.CharField(max_length=100)
    default_value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Income(models.Model):
    income_type = models.ForeignKey(IncomeType, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)

# Create your models here.
