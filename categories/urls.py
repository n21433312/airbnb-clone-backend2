from django.urls import path
from . import views

urlpatterns = [
    path(
        "", 
        views.CategoryViewSet.as_view(
            {
                "get": "list",
                "post":"create",
            }
        ),
    ),
    
    path(
        "<int:pk>", #ViewSet은 pk를 반드시 받기때문에 반드시 넣어줘야한다
        views.CategoryViewSet.as_view(
            {
                "get":"retrieve",
                "put":"partial_update",
                "delete":"destroy",
            }
        ),
    )

]