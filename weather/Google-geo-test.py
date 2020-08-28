from geolocation.main import GoogleMaps 
from geolocation.distance_matrix.client import DistanceMatrixApiClient

key = "AIzaSyDW49kSJkSbUMIp0OVs7A8nNrE57iAecog"

google_maps = GoogleMaps(api_key=key)
location = google_maps.search(location="address")
print(location.all())
my_location=location.first()

print(my_location.city)
print(my_location.route)
print(my_location.street_number)
print(my_location.postal_code)