from django.db import models

class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True, ) # object create
    updated_at = models.DateTimeField(auto_now=True) # object save

    class Meta: #장고가 모델을 확인해도DB에 저장하지 않음, 다른app에서 재사용하기 위한 class
        abstract = True