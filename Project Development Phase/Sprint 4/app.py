import json
import time

import wiotp.sdk.device

myconfig = {
    "identity" : {
        "orgId": "tn3xmm",
        "typeId": "locator",
        "deviceId": "050701"
    },
    "auth" : {
        "token" : "12345678"
    }
}
client = wiotp.sdk.device.DeviceClient(config=myconfig, logHandlers=None)
client.connect()

while True:
    city = "London"
    lat = 51.509865
    long = -0.118092

    data = {'name':city, 'lat':lat, 'lon':long}
    client.publishEvent(eventId="Active", msgFormat="json", data=data, qos=0, onPublish=None)
    print("Data Updated to IBM Platform: ", data)
    time.sleep(60)

client.disconnect()
