from django.db import models
from common.models import CommonModel


class Category(CommonModel):

    """ Room or Experiene Category"""
    
    class CategoryKindChoices(models.TextChoices):
        ROOMS = "rooms", "Rooms"
        EXPERIENCES = "experiences", "Experiences"



    name = models.CharField(max_length=50, )
    kind = models.CharField(max_length=15, choices=CategoryKindChoices.choices, )


    def __str__(self) -> str:
        return f"{self.kind.title()}: {self.name}" #title은 첫글자 대문자로
    
    class Meta:
        verbose_name_plural = "Categories"