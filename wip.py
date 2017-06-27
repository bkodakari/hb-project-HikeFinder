import requests
from secrets import transit_and_trails_api_key as key
### need help importing keys


def get_list_of_trails(latitude, longitude, distance=10):
    r = requests.get("https://api.transitandtrails.org/api/v1/trailheads", params={
        "key": key,
        "latitude": latitude,
        "longitude": longitude,
        "distance": distance
        }
        )
    # r is a response ojbect

    # /api/v1/trailheads/[id]/attributes
    # /api/v1/trailheads/[id]/photos
    # /api/v1/trailheads/[id]/maps

    trails = r.json

    dict_of_trails = {}

    for trail in trails:
        name = trail['name']
        latitude = trail['latitude']
        longitude = trail['longitude']
        description = trail['description']
        park_name = trail['park_name']
        trail_id = trail['id']
        dict_of_trails[name] = (latitude, longitude, description, park_name, trail_id)

    return dict_of_trails.keys()

def get_attributes_of_trails(trail_id):
    # r = requests.get("https://api.transitandtrails.org/api/v1/trailheads/<trail_id>/attributes", params={
    # "key": key})

    trail_id = dict_of_trails[name][trail_id]
    link = "https://api.transitandtrails.org/api/v1/trailheads/%i/attributes" % (trail_id)
    r = requests.get(link, params={"key": key})
    ## returned: <bound method Response.json of <Response [200]>>
