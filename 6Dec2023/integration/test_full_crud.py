import requests
import pytest


def get_single_booking_after_delete_get(booking_id):
    base_url = "https://restful-booker.herokuapp.com/booking/"
    endpoint = str(booking_id)
    full_url = base_url + endpoint

    headers = {"Content-Type": "application/json",
               "Accept": "application/json"}

    # Send GET request
    get_response = requests.get(url=full_url, headers=headers)
    print(get_response.text)

    # Assertions
    # assert get_response.headers["Content-Type"].__contains__("application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + get_response.headers["Content-Type"]
    assert get_response.status_code == 404, "Request failed. Expected: 404, Actual:" + str(get_response.status_code)


def delete_booking_delete(token, booking_id):
    base_url = "https://restful-booker.herokuapp.com/booking/"
    endpoint = str(booking_id)
    full_url = base_url + endpoint

    cookie = "token=" + str(token)

    headers = {"Content-Type": "application/json",
               "Cookie": cookie}

    # Send DELETE request
    delete_response = requests.delete(url=full_url, headers=headers)
    print(delete_response.text)

    # Assertions
    # assert delete_response.headers["Content-Type"].__contains__("application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + delete_response.headers["Content-Type"]
    assert delete_response.status_code == 201, "Request failed. Expected: 201, Actual:" + str(delete_response.status_code)


def full_update_booking_put(token, booking_id):
    base_url = "https://restful-booker.herokuapp.com/booking/"
    endpoint = str(booking_id)
    full_url = base_url + endpoint

    cookie = "token=" + str(token)

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


def partial_update_booking_patch(token, booking_id):
    base_url = "https://restful-booker.herokuapp.com/booking/"
    endpoint = str(booking_id)
    full_url = base_url + endpoint

    cookie = "token=" + str(token)

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


def create_token():
    base_url = "https://restful-booker.herokuapp.com/auth/"

    headers = {"Content-Type": "application/json"}

    payload = {
        "username": "admin",
        "password": "password123"
    }

    # Send POST request
    post_response = requests.post(url=base_url, headers=headers, json=payload)
    print(post_response.json())

    token = post_response.json()["token"]
    return token


def get_single_booking_get(booking_id):
    base_url = "https://restful-booker.herokuapp.com/booking/"
    endpoint = str(booking_id)
    full_url = base_url + endpoint

    headers = {"Content-Type": "application/json",
               "Accept": "application/json"}

    # Send GET request
    get_response = requests.get(url=full_url, headers=headers)
    print(get_response.json())

    # Assertions
    assert get_response.headers["Content-Type"].__contains__("application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + get_response.headers["Content-Type"]
    assert get_response.status_code == 200, "Request failed. Expected: 200, Actual:" + str(get_response.status_code)


def create_booking_post():
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


@pytest.mark.start
def test_main():
    print("Create new booking:", end=" ")
    booking_id = str(create_booking_post())
    print("New Booking ID:", booking_id)

    print("Get booking details:", end=" ")
    get_single_booking_get(booking_id)

    print("Create new token:", end=" ")
    token = str(create_token())
    print("Token details:", token)

    print("Perform partial update:", end=" ")
    partial_update_booking_patch(token, booking_id)

    print("Perform full update:", end=" ")
    full_update_booking_put(token, booking_id)

    print("Delete booking:", end=" ")
    delete_booking_delete(token, booking_id)

    print("Check if booking is present after deleting:", end=" ")
    get_single_booking_after_delete_get(booking_id)
