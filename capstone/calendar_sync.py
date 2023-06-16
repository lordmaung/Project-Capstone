import requests

calendar_id = "revier1234567@gmail.com"
API_KEY = "AIzaSyBdhuhvB16I8hWMpIisBTpQtE3YS6bfSqs"

def get_google_calendar_events(calendar_id, API_KEY):
    url = f"https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events?key={API_KEY}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        events = data.get("items", [])
        for event in events:
            event_id = event.get("id")
            summary = event.get("summary")
            start = event.get("start", {}).get("dateTime")
            end = event.get("end", {}).get("dateTime")
            print(f"Event ID: {event_id}")
            print(f"Summary: {summary}")
            print(f"Start: {start}")
            print(f"End: {end}")
            print("---")
    else:
        print("Gagal mendapatkan data acara.")

get_google_calendar_events(calendar_id, API_KEY)
