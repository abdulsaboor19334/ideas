from django.urls import path

from .views import single_instructor, all_instructors


urlpatterns = [
    path('all/', all_instructors, name='all'),
    path('<id>/', single_instructor, name='single'),
]