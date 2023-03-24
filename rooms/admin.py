from django.contrib import admin
from .models import Room, Amenity

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    
    list_display = (
        "name",
        "price",
        "kind",
        "owner",
    )

    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
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