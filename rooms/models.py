from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):
    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """RoomType model definition"""
    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):
    """Amenity model definition"""
    pass


class HouseRule(AbstractItem):
    """HouseRule model definition """
    pass


class Facility(AbstractItem):
    """Facility model definition"""
    pass


class Photo(core_models.TimeStampedModel):
    """Photo model definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """room model Definitions"""

    name = models.CharField(max_length=160)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80, default='')
    address = models.CharField(max_length=140)
    price = models.IntegerField()
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField() 
    baths = models.IntegerField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    instant_books = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", related_name="rooms", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)
