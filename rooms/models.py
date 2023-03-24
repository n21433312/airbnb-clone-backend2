from django.db import models
from common.models import CommonModel

class Room(CommonModel):

    """ Romm Model Difinition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire_Place")
        PRIVATE_ROOM = ("private_room", "Private_Room")
        SHARED_ROOM = ("shared_room", "Shared_Room")

    name = models.CharField(max_length=180, default="", )
    country = models.CharField(max_length=50, default="한국", )
    city = models.CharField(max_length=80, default="서울", )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilet = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250, )
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(max_length=20, choices=RoomKindChoices.choices, )
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, )
    amenities = models.ManyToManyField("rooms.Amenity", )

    def __str__(self):
        return self.name


class Amenity(CommonModel):

    """Amenity Definition"""

    name = models.CharField(max_length=150, )
    description = models.CharField(max_length=150, default="", blank=True) #default ="" 또는 null=True, 앞은DB가 null가능하다 뒤는 Django from에서 공백이 가능하다 서로 다름

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Amenities"