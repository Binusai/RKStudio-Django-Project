from django.shortcuts import render, redirect
from .models import Booking

def booking_view(request):
    if request.method == "POST":
        Booking.objects.create(
            session_type = request.POST.get("session_type"),
            date         = request.POST.get("date"),
            time         = request.POST.get("time"),
            name         = request.POST.get("name"),
            email        = request.POST.get("email"),
            phone        = request.POST.get("phone", "")
        )

        return redirect("/booking/#success-message")
    return render(request, "booking.html")

