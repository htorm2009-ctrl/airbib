import django_filters
from .models import Room

class RoomFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Room
        fields = ['room_type', 'room_status', 'price_min', 'price_max']
