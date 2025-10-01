from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact, name='contact'),
    path('Jewelry/',views.jewelry,name='Jewelry'),
    path('Portrait/',views.portrait,name='Portrait'),
    path('Marriage/',views.marriage,name='Marriage'),
    path('Birthday/',views.birthday,name='Birthday'),
    path('PreWedding/',views.pre,name='PreWedding'),
    path('Clothing/',views.clothing,name='Clothing'),
    path('AutoMobile/',views.auto,name='AutoMobile'),
    path('Business/',views.business,name='Business'),
    path('Frames/',views.frames,name="Frames"),
    path('Privacy/',views.privacy,name="Privacy"),
    path('Refund/',views.refund,name="Refund"),
    
]
