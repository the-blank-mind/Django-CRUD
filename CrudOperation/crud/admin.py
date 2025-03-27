from django.contrib import admin
from .models import Employee

# @admin.register(Employee)
# class adminEmp(admin.ModelAdmin)
#     list_display =('id','name','email','pwd')

admin.site.register(Employee)