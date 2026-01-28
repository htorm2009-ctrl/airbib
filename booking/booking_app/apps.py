from django.apps import AppConfig

class BookingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking_app'

    def ready(self):
        # относительный импорт из текущей папки приложения
        from . import translation
