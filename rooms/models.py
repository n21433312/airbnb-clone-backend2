from django.db import models

class Romm(models.Model):

    """ Romm Model Difinition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire_Place")
        PRIVATE_ROOM = ("private_room", "Private_Room")
        SHARED_ROOM = ("shared_room", "Shared_Room")

    country = models.CharField(max_length=50, default="한국", )
    city = models.CharField(max_length=80, default="서울", )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilet = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_langth=250, )
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(max_length=20, choices=RoomKindChoices, )
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, )
    amenities = models.ManyToManyField("rooms.Amenity", )

    class Amenity(models.Model):

        """Amenity Definition"""

        name = models.CharField(max_length=150, )
        description = models.CharField(max_length=150, default="", ) #default ="" 또는 null=True

