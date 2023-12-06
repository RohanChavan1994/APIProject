import requests
import pytest
from test_create_booking_post import test_create_booking_post
from test_create_token import test_create_token


@pytest.mark.positive
def test_partial_update_booking_patch():
    base_url = "https://restful-booker.herokuapp.com/booking/"
    endpoint = str(test_create_booking_post())
    full_url = base_url + endpoint

    cookie = "token=" + str(test_create_token())

    headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "Cookie": cookie}

    payload = {
        "firstname": "Felix",
        "lastname": "Leiter",
        "additionalneeds": "Dinner"
    }

    # Send PATCH request
    patch_response = requests.patch(url=full_url, headers=headers, json=payload)
    print(patch_response.json())

    # Assertions
    assert patch_response.headers["Content-Type"].__contains__("application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + patch_response.headers["Content-Type"]
    assert patch_response.status_code == 200, "Request failed. Expected: 200, Actual:" + str(patch_response.status_code)
