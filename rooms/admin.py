from django.contrib import admin
from .models import Room, Amenity

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )



    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "owner__username", #^onwer__username으로 하면 시작하는 단어로 검색가능startswith,=owner_username는 완전히 동일한 값 검색
    )

    
        


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )

    readonly_fields = ( #수정불가 필드
        "created_at",
        "updated_at",

    )