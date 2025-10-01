from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from booking.models import Booking
# Create your views here.

OWNER_PASSWORD = "rkstudio1234amjad"

def dashboard_login(request):
    if request.method == "POST":
        password = request.POST.get("password")
        if password == OWNER_PASSWORD:
            request.session["dashboard_auth"] = True
            return redirect("dashboard_home")
        else:
            return render(request, "dashboard_login.html", {"error": "Invalid password"})
    return render(request, "dashboard_login.html")

def dashboard_home(request):
    if not request.session.get("dashboard_auth"):
        return redirect("dashboard_login")

    if request.method == "POST":
        booking_id = request.POST.get("booking_id")
        action = request.POST.get("action")  
        booking = get_object_or_404(Booking, id=booking_id)
        contact_number = "+91-9440516707"  

        if action == "accept":
            booking.status = "Accepted" 
            booking.save()
            subject = "Booking Accepted - RK Studio"
            message = f"""
Hello {booking.name},

Thank you for choosing RK Studio! We are happy to confirm your booking.

Booking Details:
Session Type: {booking.session_type}
Date: {booking.date}
Time: {booking.time}

We look forward to capturing your special moments! 
If you need any further assistance, please contact us at {contact_number}.

Best regards,
RK Studio Team
"""
        elif action == "reject":
            booking.status = "Rejected" 
            booking.save()
            subject = "Booking Status - RK Studio"
            message = f"""
Hello {booking.name},

Thank you for reaching out to RK Studio. 
Unfortunately, we are fully booked at the requested date/time.

If you are flexible with another date, please contact us at {contact_number} to reschedule.

We apologize for the inconvenience and hope to serve you soon.

Best regards,
RK Studio Team
"""

        elif action == "delete":
            booking.delete()
            return redirect("dashboard_home")
    
        else:
            return redirect("dashboard_home")

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [booking.email],
            fail_silently=False,
        )

        return redirect("dashboard_home")

    bookings = Booking.objects.all().order_by('-submitted_at')

    return render(request, "dashboard.html", {"bookings": bookings})

def dashboard_logout(request):
    request.session.flush()
    return redirect("dashboard")

