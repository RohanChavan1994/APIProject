import requests


def main():
    try:
        response1 = requests.get("https://restful-booker.herokuapp.com/booking")
        id = response1.json()[0]["bookingid"]
        print(id)
        response2 = requests.get("https://restful-booker.herokuapp.com/booking/" + str(id))
        response_body = response2.json()
        print(response_body)

        # Assertions
        # Verification of keys
        assert "firstname" in response_body, "Firstname is not present"
        assert "lastname" in response_body, "Lastname is not present"

        # Verification of data
        assert response2.status_code == 200, "Invalid status code. Expected: 200, Actual:" + str(response2.status_code)
        assert response_body["firstname"] == "John", "Invalid first name. Expected: John, Actual:" + response_body["firstname"]
    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()
