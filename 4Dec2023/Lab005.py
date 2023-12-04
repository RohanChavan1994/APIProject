import json
import requests

payload_str = dict({
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
})

try:
    # payload = json.loads(payload_str)
    response = requests.post(url="https://restful-booker.herokuapp.com/booking", data=payload_str,
                             headers={"Content-Type": "application/json",
                                      "Accept": "application/json"})
    print(response.status_code)
    print(response.text)
except Exception as error:
    print(error)
