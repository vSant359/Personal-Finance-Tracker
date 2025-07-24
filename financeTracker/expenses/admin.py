from django.contrib import admin
from .models import Expense, DefaultExpense

""" This option is not necessary in this moment, but i think i can use this in the future:

@admin.register(ExpenseType)
class ExpenseTypeAdmin(admin.ModelAdmin):
    pass
    
"""

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'date', 'created_at')
    list_filter = ('category', 'date')
    search_fields = ('title', 'description')
    ordering = ('-date',)

@admin.register(DefaultExpense)
class DefaultExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'description', 'active')
    list_filter = ('name', 'active')
    search_fields = ('title', 'description')
    
