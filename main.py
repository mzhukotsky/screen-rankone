from utils.rankone_api import get_profile_events

def main():
    username = "slexboy"
    profile_events = get_profile_events(username)
    if profile_events:
        
        print(profile_events)

if __name__ == "__main__":
    main()