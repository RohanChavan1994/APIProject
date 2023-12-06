import requests
import pytest
from test_create_booking_post import test_create_booking_post
from test_create_token import test_create_token


@pytest.mark.positive
def test_full_update_booking_put():
    base_url = "https://restful-booker.herokuapp.com/booking/"
    endpoint = str(test_create_booking_post())
    full_url = base_url + endpoint

    cookie = "token=" + str(test_create_token())

    headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "Cookie": cookie}

    payload = {
        "firstname": "Vesper",
        "lastname": "Lynd",
        "totalprice": 400,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-12-22",
            "checkout": "2024-1-2"
        },
        "additionalneeds": "Breakfast, Lunch, Dinner"
    }

    # Send PUT request
    put_response = requests.put(url=full_url, headers=headers, json=payload)
    print(put_response.json())

    # Assertions
    assert put_response.headers["Content-Type"].__contains__("application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + put_response.headers["Content-Type"]
    assert put_response.status_code == 200, "Request failed. Expected: 200, Actual:" + str(put_response.status_code)
