# travel_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class DestinationSuggestions(APIView):
    def post(self, request):
        destination = request.data.get('destination')
        # For this example, we'll use a mock API response
        mock_data = [
            {"name": f"{destination} Beach Resort", "location_string": f"{destination}, Tropical Island"},
            {"name": f"{destination} Mountain Retreat", "location_string": f"{destination}, Mountain Range"},
            {"name": f"{destination} City Center Hotel", "location_string": f"{destination}, Downtown"},
        ]
        return Response({"data": mock_data})