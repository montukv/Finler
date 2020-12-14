from django.contrib import admin
from expense_tracker.models import ExpenseInfo
# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
      list_display    = ['expense_name', 'cost', 'date_added', 'user_expense']

admin.site.register(ExpenseInfo)
