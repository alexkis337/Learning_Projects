import requests
import numpy as np


list_of_hcos = ['AP-HM Marseille', 'Hôpital Necker-Enfants Malades'
]

result = {}


def get_address(location_name):
    # Google Maps API endpoint
    endpoint = "https://maps.googleapis.com/maps/api/geocode/json?"

    # API key
    API_KEY = "AIzaSyBzA3c6mq1LXGih5e9_L-06QP55qzYQ6ng"

    # build the URL for the API request
    url = endpoint + "address=" + location_name + "&key=" + API_KEY

    # make the API request
    response = requests.get(url)

    # check the status code of the response
    if response.status_code == 200:
        try: # get the address from the response
            address = response.json()["results"][0]["formatted_address"]
            return address
        except:
            pass
    else:
        return None


for hco in list_of_hcos:
    try:
        result[hco] = get_address(hco)
    except IndexError:
        result[hco] = ''

print(result)


def get_location(address):
    # Google Maps API endpoint
    endpoint = "https://maps.googleapis.com/maps/api/geocode/json?"

    # API key
    API_KEY = "AIzaSyBzA3c6mq1LXGih5e9_L-06QP55qzYQ6ng"

    # build the URL for the API request
    url = endpoint + "address=" + address.replace(" ", "+") + "&key=" + API_KEY

    # make the API request
    response = requests.get(url)

    # check the status code of the response
    if response.status_code == 200:
        # get the location information from the response
        location_data = response.json()["results"][0]["geometry"]["location"]
        return location_data
    else:
        return None


def get_coordinates(location_name):
    # Google Maps API endpoint
    endpoint = "https://maps.googleapis.com/maps/api/geocode/json?"

    # API key
    API_KEY = "AIzaSyBzA3c6mq1LXGih5e9_L-06QP55qzYQ6ng"

    # build the URL for the API request
    url = endpoint + "address=" + location_name + "&key=" + API_KEY

    # make the API request
    response = requests.get(url)

    # check the status code of the response
    try:
        if response.status_code == 200:
            # get the coordinates from the response
            lat = response.json()["results"][0]["geometry"]["location"]["lat"]
            lng = response.json()["results"][0]["geometry"]["location"]["lng"]
            return (lat, lng)
        else:
            return None
    except IndexError:
        return None


# get the address for a location name
# location_name = 'APHM HOPITAL LA TIMONE ADULTES'
# address = get_address(location_name)


for hco in list_of_hcos:
    print(hco)
    result[hco] = get_address(hco)

print(result)


# result_hco_coord = result
# #print(result)
#
#
# for hco in result_hco_coord:
#     location = get_location(result_hco_coord[hco])
#     result_hco_coord[hco] = [round(location["lat"], 6), round(location["lng"], 6)]
#
# for brick in list_of_addresses:
#     location = get_location(brick)
#     result_adr_coord[brick] = [round(location["lat"], 6), round(location["lng"], 6)]
#
#
# print(result_hco_coord)
# print(result_adr_coord)
# fin_res = {}
#
# for adr in result_adr_coord:
#     for hco in result_hco_coord:
#         if np.sqrt((result_adr_coord[adr][0] - result_hco_coord[hco][0])**2 +
#                    (result_adr_coord[adr][1] - result_hco_coord[hco][1])**2) < 0.0055:
#             fin_res[adr] = hco
#             break
#         else:
#             fin_res[adr] = 'no address found'
#
# print(fin_res)

## print the address
#if address:
#    print("Address:", address)
#else:
#    print("Address not found.")