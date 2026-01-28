from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class Country(models.Model):
    country = models.CharField(max_length=10, unique=True)
    country_image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.country


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)],
                                           null=True, blank=True)
    user_image = models.ImageField(upload_to='user_photo', null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    RoleChoices = (
    ('client', 'client'),
    ('owner', 'owner'),
    )
    role = models.CharField(max_length=10, choices=RoleChoices, default='client')
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class City(models.Model):
    city = models.CharField(max_length=10, unique=True)
    city_image = models.ImageField(upload_to='city_photo', null=True, blank=True)

class Service(models.Model):
    service_image = models.ImageField(upload_to='service_photo', null=True, blank=True)
    service = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.service_image}, {self.service}'

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=10, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    postal_code = models.PositiveIntegerField(verbose_name="Postal Code")
    hotel_stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    description = models.TextField()
    hotel_service = models.ManyToManyField(Service)

    def __str__(self):
        return self.hotel_name

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel_image = models.ImageField(upload_to='hotel_image',)

    def __str__(self):
        return f'{self.hotel}, {self.hotel_image}'

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField()
    RoomTypeChoices = (
        ('Люкс', 'Люкс'),
        ('ПолуЛюкс', 'ПолуЛюкс'),
        ('Семейный', 'Семейный'),
        ('Эконом', 'Эконом'),
        ('Одноместный','Одноместный')
    )
    room_type = models.CharField(max_length=20, choices=RoomTypeChoices)
    RoomStatus = (
    ('Занят','Занят'),
    ('Забронирован','Забронирован'),
    ('Свободен','Свободен'),
    )
    room_status = models.CharField(max_length=20, choices=RoomStatus)
    description = models.TextField()

    def __str__(self):
        return f'{self.room_number}, {self.room_type}, {self.room_status}, {self.RoomStatus}'


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='room_image',)

    def __str__(self):
        return f'{self.room}, {self.room_image}'

class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i,str(i))for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.comment}, {self.hotel}'

class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_out = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.room}, {self.check_out}'





