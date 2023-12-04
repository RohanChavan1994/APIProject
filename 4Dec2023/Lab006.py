import requests


def main():
    try:
        response = requests.get(url="https://restful-booker.herokuapp.com/booking/2473")
        print(response.text)
        print(response.status_code)
        print(response.headers["Content-Type"])
    except Exception as error:
        print("Error occurred:", error)


if __name__ == "__main__":
    main()
