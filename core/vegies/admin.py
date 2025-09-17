from django.contrib import admin

# Register your models here.
from .models import Receipe


@admin.register(Receipe)
class ReceipeAdmin(admin.ModelAdmin):
    list_display = ('receipe_name','receipe_description','receipe_image')