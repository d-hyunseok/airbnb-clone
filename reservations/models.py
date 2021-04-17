from django.db import models
from core import models as core_models


class Reservation(core_models.TimeStampedModel):

    """reservations model definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICE = (
        (STATUS_PENDING, "pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_CANCELED, "canceled"),
    )

    status = models.CharField(max_length=12, choices=STATUS_CHOICE, default=STATUS_PENDING)

    check_in = models.TimeField()
    check_out = models.TimeField()

    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.room} - {self.check_in}'
