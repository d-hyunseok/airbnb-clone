from django.contrib import admin
from . import models


@admin.register(models.Notices)
class NoticeAdmin(admin.ModelAdmin):

    pass
