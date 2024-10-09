import requests

API_KEY = "e249f0db4729d85abc3a176cc70128f0"


def get_data(place, days, option):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    return content


if __name__ == "__main__":
    data = get_data("Tokyo", None, None)
    print(data)
