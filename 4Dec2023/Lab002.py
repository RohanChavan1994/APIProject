import requests


def main():
    try:
        response = requests.get("https://restful-booker.herokuapp.com/booking")
        assert response.status_code == 200, "Invalid status code. Expected: 200, Actual:" + str(response.status_code)
    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()
