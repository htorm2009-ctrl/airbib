from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import *


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CountryListSerializer
        return CountryDetailSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CityListSerializer
        return CityDetailSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    pagination_class = HotelPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['country', 'city', 'hotel_stars', 'hotel_service']
    search_fields = ['hotel_name']
    ordering_fields = ['hotel_stars']

    def get_serializer_class(self):
        if self.action == 'list':
            return HotelListSerializer
        return HotelDetailSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    pagination_class = RoomPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['room_type', 'room_status']
    search_fields = ['room_number']
    ordering_fields = ['price']


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
