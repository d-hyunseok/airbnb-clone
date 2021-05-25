from django.db import models


class Notice(models.Model):

    title = models.CharField(max_length=80)
    content = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
