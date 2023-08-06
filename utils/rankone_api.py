import requests

def get_profile_events(profile_name):
    url = profile_name
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            events_data = data.get('events', {}).get('entries', [])
            return events_data
        else:
            print(f"Ошибка при запросе: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None
