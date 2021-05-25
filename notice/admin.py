from django.contrib import admin
from . import models


@admin.register(models.Notice)
class NoticeAdmin(admin.ModelAdmin):

    list_display = ("title", "user", "created_at")
