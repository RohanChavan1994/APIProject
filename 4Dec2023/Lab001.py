import requests


def main():
    response = requests.get("https://restful-booker.herokuapp.com/booking")
    if response.status_code == 200:
        print("Successful request")
    else:
        print("Request failed")


if __name__ == '__main__':
    main()
    