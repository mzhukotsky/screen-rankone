import requests

def get_profile_events(profile_name):
    url = profile_name
    try:
        response = requests.get(url)
        # print(response.status_code)  # Вывести статус-код ответа
        # print(response.text)

        if response.status_code == 200:
            data = response.json()
            profile_data = data.get("events", {})
            return profile_data
        else:
            print(f"Error while taking request: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error while executing request: {e}")
        return None
