import n2yo_api
import network_connect
#import motor_control
import json
import time

def get_config_satellite():
    with open("config.json") as file:
        config = json.load(file)
        sat_id = config['satellite']['sat_id']
        latitude = config['satellite']['latitude']
        longitude = config['satellite']['longitude']
        altitude = config['satellite']['altitude']
        seconds = config['satellite']['seconds']
        api_key = config['satellite']['api_key']
        delay = int(config['satellite']['delay'])
    return sat_id, latitude, longitude, altitude, seconds, api_key, delay
    
def get_config_wifi():
    with open("config.json") as file:
        config = json.load(file)
        ssid = config['network']['ssid']
        password = config['network']['password']
    return ssid, password

sat_id, latitude, longitude, altitude, seconds, api_key, delay = get_config_satellite()
ssid, password = get_config_wifi()

url = "https://api.n2yo.com/rest/v1/satellite/positions/{}/{}/{}/{}/{}&apiKey={}".format(
    sat_id, latitude, longitude, altitude, seconds, api_key
)
network_connect.connect_wifi(ssid=ssid, password=password)

while True:
    try:
        azimuth, elevation = n2yo_api.obtain_data(url=url)
    except Exception as e:
        print("Error: {}".format(e))
        break
    print("Azimuth: {} Elevation: {}".format(azimuth, elevation))
    #motor_control.update_position(azimuth, elevation)
    time.sleep(delay)
