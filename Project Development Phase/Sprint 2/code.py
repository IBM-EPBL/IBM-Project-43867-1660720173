import json
import wiotp.sdk.device
import time

myconfig = {
    "identity" : {
        "orgId": "tn3xmm",
        "typeId": "SM32",
        "deviceId": "1234"
    },
    "auth" : {
        "token" : "12345678"
    }
}
client = wiotp.sdk.device.DeviceClient(config=myconfig, logHandlers=None)
client.connect()

while True:
    city = "London"
    lat = 34.8976508
    long = 67.9764532

    data = {'name':city, 'lat':lat, 'lon':long}
    client.publishEvent(eventId="Active", msgFormat="json", data=data, qos=0, onPublish=None)
    print("Data Updated to IBM Platform: ", data)
    time.sleep(3)

client.disconnect()