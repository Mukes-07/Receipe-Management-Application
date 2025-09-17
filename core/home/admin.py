from django.contrib import admin

from .models import Student, Product, Car

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'address')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'speed')