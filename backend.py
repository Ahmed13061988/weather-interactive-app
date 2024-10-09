import requests

API_KEY = "e249f0db4729d85abc3a176cc70128f0"


def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    filtered_content = content["list"]
    filtered_content = filtered_content[:8 * days]
    return filtered_content


if __name__ == "__main__":
    data = get_data("Tokyo", 3)
    print(data)
