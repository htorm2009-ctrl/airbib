from .models import Country, City, Service, Hotel, Room, Review
from modeltranslation.translator import TranslationOptions, register

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country',)

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city',)

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('service',)

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'street', 'description',)

@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment',)
