from django.db import models
from common.models import CommonModel

class Photo(CommonModel):

    file = models.URLField()
    description = models.CharField(max_length=150, )
    room = models.ForeignKey("rooms.Room", null=True, blank=True, on_delete=models.CASCADE, )
    experience = models.ForeignKey("experiences.Experience", null=True, blank=True, on_delete=models.CASCADE, )
    
    def __str__(self):
        return "Photo File"



class Video(CommonModel):

    file = models.URLField()
    experience = models.OneToOneField("experiences.Experience", on_delete=models.CASCADE, ) #ForeignKey랑 같지만 고유한 값이된다. 활동 하나가 영상을 가지면 더 가질 수 없다
       
    def __str__(self):
        return "Video File"