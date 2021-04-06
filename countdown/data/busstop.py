from requests import get, post, put
from pathlib import Path


def get_postcode_info(postcode="NW51TL"):
# api.postcodes.io/postcodes/NW51TL
    # if postcode  
    # postcode = "NW51TL"
    postcode = postcode.replace(" ", "")
    endpoint = ('https://api.postcodes.io/postcodes/' + postcode)
    response = get(endpoint, timeout=10)
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: {response.text}')

    postcode_data = response.json()
    # print(postcode_data['result']['longitude'])

    # print(postcode_data['result']['latitude'])
    # postcode
    return postcode_data['result']['longitude'], postcode_data['result']['latitude']


def get_bus_info(this_code):
    param = {'app_id': "a3507441", 'app_key': "f60f2bac8956a26e0318b6960e7daa9f"}

        # &app_id=a3507441&app_key=f60f2bac8956a26e0318b6960e7daa9f
    
    output_list=[]
    # for this_code in codeList:
    endpoint = ("http://transportapi.com/v3/uk/bus/stop/"+ this_code + "/live.json")
    response = get(endpoint, data = param, timeout=10)
    data = response.json()

    line = next(iter(data['departures']))

    directions = data['departures'][line][0]['direction']
    expected = data['departures'][line][0]['expected_departure_time']

    return line, directions, expected


def get_bus_code(long, lat):
    

    param = {'app_id': "a3507441", 'app_key': "f60f2bac8956a26e0318b6960e7daa9f"}
    endpoint = ("http://transportapi.com/v3/uk/places.json?lat=" + lat + "&lon=" + long + "&type=bus_stop")
    response = get(endpoint, data = param, timeout=10)

    bus_data = response.json()

    data = bus_data["member"]
    # print("First data entry ", data[0]["atcocode"])
    # print("Second data entry", data[1]["atcocode"])

    return data[0]["atcocode"], data[1]["atcocode"]

    # gets the data for the nearest bus stops
    # http://transportapi.com/v3/uk/places.json?lat=51.553935&lon=-0.144754&type=bus_stop&app_id=a3507441&app_key=f60f2bac8956a26e0318b6960e7daa9f

    # gets the live data for a particular stop with it's atcocode (unique identifier)
    # http://transportapi.com/v3/uk/bus/stop/{atcocode}/live.json&app_id=a3507441&app_key=f60f2bac8956a26e0318b6960e7daa9f


if __name__ == "__main__":
    # codeList = get_bus_code()
    # for this_code in codeList:
    #     print(get_bus_info(this_code))
    get_postcode_info()