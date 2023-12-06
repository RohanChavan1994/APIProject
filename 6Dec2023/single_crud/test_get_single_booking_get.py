import requests
import pytest
from test_create_booking_post import test_create_booking_post


@pytest.mark.positive
def test_get_single_booking_get():
    base_url = "https://restful-booker.herokuapp.com/booking/"
    endpoint = str(test_create_booking_post())
    full_url = base_url + endpoint

    headers = {"Content-Type": "application/json",
               "Accept": "application/json"}

    # Send GET request
    get_response = requests.get(url=base_url, headers=headers)
    print(get_response.json())

    # Assertions
    assert get_response.headers["Content-Type"].__contains__("application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + get_response.headers["Content-Type"]
    assert get_response.status_code == 200, "Request failed. Expected: 200, Actual:" + str(get_response.status_code)
