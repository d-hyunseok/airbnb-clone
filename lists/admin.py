from django.contrib import admin
from  . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    """list admin definition"""
    list_display = ("name", "user",)