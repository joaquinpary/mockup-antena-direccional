import network  # type: ignore
import time
import machine  # type: ignore

def connect_wifi(ssid, password):
    ssid = str(ssid)
    password = str(password)
    
    wlan = network.WLAN(mode=network.WLAN.STA)
    wlan.deinit()
    time.sleep(1)
    wlan.init(mode=network.WLAN.STA)  
    wlan.connect("{}".format(ssid), (network.WLAN.WPA2, "{}".format(password)))

    for _ in range(10):
        if wlan.isconnected():
            print("Connected! IP:", wlan.ifconfig()[0])
            break
        time.sleep(1)
    else:
        print("Error: Could not connect to the network")
        machine.reset()

