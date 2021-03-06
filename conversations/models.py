from django.db import models
from core import models as core_models


class Conversations(core_models.TimeStampedModel):

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):

    message = models.TimeField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversations", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} say : {self.text}'