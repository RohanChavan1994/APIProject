import requests


def test_create_token():
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
