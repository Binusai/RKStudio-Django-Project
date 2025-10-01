from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'session_type', 'date', 'time', 'email', 'phone', 'submitted_at')
