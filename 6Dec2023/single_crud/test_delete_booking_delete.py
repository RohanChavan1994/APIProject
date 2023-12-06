import requests
import pytest
from test_create_booking_post import test_create_booking_post
from test_create_token import test_create_token


@pytest.mark.positive
def test_delete_booking_delete():
    base_url = "https://restful-booker.herokuapp.com/booking/"
    endpoint = str(test_create_booking_post())
    full_url = base_url + endpoint

    cookie = "token=" + str(test_create_token())

    headers = {"Content-Type": "application/json",
               "Cookie": cookie}

    # Send DELETE request
    delete_response = requests.delete(url=full_url, headers=headers)
    print(delete_response.text)

    # Assertions
    # assert delete_response.headers["Content-Type"].__contains__("application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + delete_response.headers["Content-Type"]
    assert delete_response.status_code == 201, "Request failed. Expected: 200, Actual:" + str(delete_response.status_code)
