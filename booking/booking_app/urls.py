from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'countries', CountryViewSet)
router.register(r'cities', CityViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'users', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('countries/<int:pk>/',CountryViewSet.as_view({'get': 'retrieve'}),name='country-detail'),
    path('cities/<int:pk>/',CityViewSet.as_view({'get': 'retrieve'}),name='city-detail'),
    path('hotels/<int:pk>/',HotelViewSet.as_view({'get': 'retrieve'}),name='hotel-detail'),
    path('accounts/', include('allauth.urls')),
]

