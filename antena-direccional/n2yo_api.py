try: 
    import urequests as requests # type: ignore
except ImportError:
    import requests


def obtain_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        #print(json.dumps(data, indent=4))
        data_azimuth = data['positions'][0]['azimuth']
        data_elevation = data['positions'][0]['elevation']
    else:
        print("Error. Status Code: {}".format(response.status_code))
    return data_azimuth, data_elevation