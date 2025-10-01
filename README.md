# RK Studio Django Backend

This directory contains the Django backend for the RK Studio photography website. The backend handles the online booking functionality.

## Project Structure

- `rk_studio/` - Main Django project directory
  - `settings.py` - Project settings
  - `urls.py` - URL configurations
  - `wsgi.py` - WSGI configuration
  - `asgi.py` - ASGI configuration
- `booking/` - Booking app directory
  - `models.py` - Contains the Booking model
  - `forms.py` - Contains the BookingForm
  - `views.py` - Contains the booking view functions
  - `urls.py` - URL patterns for the booking app
  - `admin.py` - Admin configurations
  - `templates/` - HTML templates
    - `booking/` - Booking app templates
      - `booking.html` - Booking form template

## Setup Instructions

1. Install Django: `pip install django`
2. Navigate to this directory: `cd django_project`
3. Run migrations: `python manage.py makemigrations` and `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Run the development server: `python manage.py runserver`
6. Access the admin panel at: `http://127.0.0.1:8000/admin/`
7. Access the booking page at: `http://127.0.0.1:8000/booking/`