import requests

API_KEY = "e249f0db4729d85abc3a176cc70128f0"


def get_data(place, days, option):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    filtered_content = content["list"]
    filtered_content = filtered_content[:8 * days]
    if option == "Temperature":
        filtered_content = [i["main"]["temp"] for i in filtered_content]
    elif option == "Sky":
        filtered_content = [i["weather"][0]["main"] for i in filtered_content]

    return filtered_content


if __name__ == "__main__":
    data = get_data("Tokyo", 3, "Sky")
    print(data)
