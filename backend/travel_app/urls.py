# travel_app/urls.py
from django.urls import path
from .views import DestinationSuggestions

urlpatterns = [
    path('suggestions/', DestinationSuggestions.as_view(), name='destination-suggestions'),
]