from django.db import models
from django.utils import timezone

class Booking(models.Model):
    SESSION_CHOICES = [
        ('jewelry', 'Jewelry Photography'),
        ('portrait', 'Portrait Photography'),
        ('wedding', 'Wedding Photography'),
        ('birthday', 'Birthday Photography'),
        ('pre_wedding','Pre-Wedding Shoots'),
        ('clothing_fashion','Clothing & Fashion Photography'),
        ('automobile','Auto-Mobile Photography'),
        ('business_professional','Business & Professional'),
    ]
    session_type = models.CharField(max_length=30, choices=SESSION_CHOICES)
    date         = models.DateField()
    time         = models.TimeField()
    name         = models.CharField(max_length=100)
    email        = models.EmailField()
    phone        = models.CharField(max_length=20, blank=True)
    submitted_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, default="Pending")

    def __str__(self):
        return f"{self.name} – {self.session_type} – {self.date}"