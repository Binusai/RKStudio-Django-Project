from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard_login,name="dashboard"),
    path('dashboard_home/',views.dashboard_home,name="dashboard_home"),
    path('dashboard_logout/',views.dashboard_logout,name="dashboard_logout"),
    
]
