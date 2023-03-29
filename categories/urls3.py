from django.urls import path
from . import views

urlpatterns = [
    path("", views.Categories.as_view()), #calss를 불러올려면 as_view를 써야함
    path("<int:pk>", views.CategoryDetail.as_view())

]