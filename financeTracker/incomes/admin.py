from django.contrib import admin
from .models import Income
from .models import IncomeType

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('income_type', 'value', 'date')
    list_filter = ('income_type', 'date')
    search_fields = ('income_type', 'description')
    ordering = ('-date',)

@admin.register(IncomeType)
class IncomeTypeAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name', 'default_value', 'created_at')
    # list_filter = ('name', 'created_at')
    # ordering = ('-date',)
# Register your models here.
