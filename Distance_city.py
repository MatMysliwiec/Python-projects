from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def coordinates(city):
    geolocator = Nominatim(user_agent="distance_calculator")
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    else:
        print(f"Could not find coordinates for {city}")
        return None


def calculate_dist(city1, city2, unit):
    coords1 = coordinates(city1)
    coords2 = coordinates(city2)

    if coords1 and coords2:
        if unit.lower().startswith("km"):
            distance = geodesic(coords1, coords2).kilometers
            return distance
        elif unit.lower().startswith("mi"):
            distance = geodesic(coords1, coords2).miles
            return distance
    else:
        return None


city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")
unit = input("Enter the unit of distance (km/mi): ")

result = calculate_dist(city1, city2, unit)
if result is not None:
    print(f"Distance between {city1} and {city2} is {result} {unit}")
else:
    print("Error")
