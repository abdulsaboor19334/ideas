from django.urls import path
from .views import front_page

urlpatterns = [
    path('front/', front_page, name='front')
]