import requests
from secrets import transit_and_trails_api_key as ttkey
from secrets import google_maps_geocode_api_key as ggkey
# from secrets import dark_sky_api_key as dskey
### need help importing keys


def get_geocode(address):
    r = requests.get("https://maps.googleapis.com/maps/api/geocode/json", params={
        "address": address,
        "key": ggkey,
        }
        )
    print "###################", r
    geocode_result = r.json()
    print geocode_result
    latitude = geocode_result["results"][0]["geometry"]["location"]["lat"]
    longitude = geocode_result["results"][0]["geometry"]["location"]["lng"]

    print latitude, longitude
    return latitude, longitude


def get_list_of_trails(latitude, longitude, distance=10):
    r = requests.get("https://api.transitandtrails.org/api/v1/trailheads", params={
        "key": ttkey,
        "latitude": latitude,
        "longitude": longitude,
        "distance": distance
        }
        )
    # r is a response ojbect

    # /api/v1/trailheads/[id]/attributes
    # /api/v1/trailheads/[id]/photos
    # /api/v1/trailheads/[id]/maps

    trails = r.json()

    dict_of_trails = {}
    list_of_trail_ids = []

    for trail in trails:
        name = trail['name']
        latitude = trail['latitude']
        longitude = trail['longitude']
        description = trail['description']
        park_name = trail['park_name']
        trail_id = trail['id']
        list_of_trail_ids += trail_id
        dict_of_trails[name] = [name, latitude, longitude, description, park_name, trail_id]

    return dict_of_trails


def get_attributes_of_trails(trail_id):
    """Make a request to get the attributes for specified trail_id."""
    # r = requests.get("https://api.transitandtrails.org/api/v1/trailheads/<trail_id>/attributes", params={
    # "key": key})

    # trail_id = dict_of_trails[name][trail_id]
    link = "https://api.transitandtrails.org/api/v1/trailheads/%i/attributes" % (trail_id)
    r = requests.get(link, params={"key": ttkey})
    attributes = r.json()
    return attributes


def get_photos_of_trails(trail_id):
    """Make a request to get photos for specified trail_id."""

    # trail_id = dict_of_trails[name][trail_id]
    link = "https://api.transitandtrails.org/api/v1/trailheads/%i/photos" % (trail_id)
    r = requests.get(link, params={"key": ttkey})
    photos = r.json()
    return photos


def get_weather_forecast(address):
        ### For Weather forecast
    # w = requests.get("https://api.darksky.net/forecast/", params={
    #     "key": dskey,
    #     "latitude": latitude,
    #     "longitude": longitude
    #     })
    ####### must be formatted as "latitude, longitude"
    ####### check out python wrapper
    pass