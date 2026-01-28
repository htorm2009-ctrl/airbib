from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *
from . import translation  # ⚠️ обязательно первым

# --- Inline ---
class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1

class RoomInline(admin.TabularInline):
    model = Room
    extra = 1

class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0

# --- TranslationAdmin Media ---
class TranslationMedia:
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

# --- Admin для моделей с переводом ---
@admin.register(Country)
class CountryAdmin(TranslationAdmin, TranslationMedia):
    list_display = ("country",)

@admin.register(City)
class CityAdmin(TranslationAdmin, TranslationMedia):
    list_display = ("city",)

@admin.register(Service)
class ServiceAdmin(TranslationAdmin, TranslationMedia):
    list_display = ("service",)

@admin.register(Hotel)
class HotelAdmin(TranslationAdmin, TranslationMedia):
    list_display = ("hotel_name", "city", "country", "hotel_stars")
    inlines = [HotelImageInline, RoomInline]

@admin.register(Room)
class RoomAdmin(TranslationAdmin, TranslationMedia):
    list_display = ("room_number", "room_type", "room_status", "hotel", "price")
    inlines = [RoomImageInline]

@admin.register(Review)
class ReviewAdmin(TranslationAdmin, TranslationMedia):
    list_display = ("user", "hotel", "rating", "created_at")

# --- Модели без перевода ---
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "role", "country", "phone_number", "age")
    inlines = [BookingInline]

@admin.register(HotelImage)
class HotelImageAdmin(admin.ModelAdmin):
    list_display = ("hotel", "hotel_image")

@admin.register(RoomImage)
class RoomImageAdmin(admin.ModelAdmin):
    list_display = ("room", "room_image")

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "hotel", "room", "check_out", "created_at")
