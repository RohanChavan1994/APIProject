import requests
import pytest


@pytest.mark.positive
def test_create_booking_post():
    base_url = "https://restful-booker.herokuapp.com/booking/"

    headers = {"Content-Type": "application/json",
               "Accept": "application/json"}

    payload = {
        "firstname": "James",
        "lastname": "Bond",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-12-22",
            "checkout": "2023-12-27"
        },
        "additionalneeds": "Breakfast"
    }

    # Send POST request
    post_response = requests.post(url=base_url, headers=headers, json=payload)
    print(post_response.json())

    # Assertions
    assert post_response.headers["Content-Type"].__contains__("application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + post_response.headers["Content-Type"]
    assert post_response.status_code == 200, "Request failed. Expected: 200, Actual:" + str(post_response.status_code)

    # Send Booking ID to next request
    booking_id = post_response.json()["bookingid"]
    return booking_id
