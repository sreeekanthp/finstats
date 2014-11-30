from django.contrib import admin

from .models import *

admin.site.register(IncomeType)
admin.site.register(ExpenseType)
admin.site.register(Income)
admin.site.register(Expense)
