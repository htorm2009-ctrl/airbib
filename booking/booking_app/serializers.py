from .models import *
from rest_framework import serializers


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'country', 'country_image')

class CountryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'city', 'city_image')

class CityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'service', 'service_image')


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ('id', 'hotel_image')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class HotelListSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    city = serializers.StringRelatedField()

    class Meta:
        model = Hotel
        fields = (
            'id',
            'hotel_name',
            'country',
            'city',
            'hotel_stars',
        )

class HotelDetailSerializer(serializers.ModelSerializer):
    country = CountryListSerializer()
    city = CityListSerializer()
    hotel_service = ServiceSerializer(many=True)
    rooms = RoomSerializer(source='room_set', many=True)
    images = HotelImageSerializer(source='hotelimage_set', many=True)

    class Meta:
        model = Hotel
        fields = (
            'id',
            'hotel_name',
            'country',
            'city',
            'street',
            'postal_code',
            'hotel_stars',
            'description',
            'hotel_service',
            'rooms',
            'images',
        )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

