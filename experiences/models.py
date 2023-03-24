from django.db import models
from common.models import CommonModel

class Experience(CommonModel):

    """Experience Model Definition"""

    country = models.CharField(max_length=50, default="한국", )
    city = models.CharField(max_length=80, default="서울", )
    name = models.CharField(max_length=250, )
    host = models.ForeignKey("users.User", on_delete=models.CASCADE, )
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250, )
    start = models.TimeField() #DateField는 년월일 TimeField는 시분초, DateTimeField는 년월일시분초
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField("experiences.Perk", )
    category = models.ForeignKey("categories.Category", blank=True, null=True, on_delete=models.SET_NULL, ) # 카테고리지워져도 Experiences가 지워지지 않게하기위해 + 값이 없어도 되게하기


    def __str__(self) -> str:
       return  self.name

class Perk(CommonModel):

    """What is included on an Experience"""

    name = models.CharField(max_length=100, )
    details = models.CharField(max_length=250,blank=True, null=True,  )
    explanation = models.TextField(blank=True, null=True)
    

    def __str__(self) -> str:
        return self.name
