from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from datetime import datetime, timedelta
import pytz

class GCalendar:

    def __init__(self, scopes) -> None:
        self.scopes = scopes
        self.creds = None
        self.service = None

    def ensure_creds(self):
        if self.service is not None:
            return
        
        if os.path.exists('token.json'):
            self.creds = Credentials.from_authorized_user_file('token.json', self.scopes)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                print("no creds yet")
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.scopes)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(self.creds.to_json())
        self.service = build('calendar', 'v3', credentials=self.creds)

    def add_event(self, event):
        """Add an event to the calendar"""

        self.ensure_creds()

        event = self.service.events().insert(calendarId='primary', body=event).execute()
        print(f"Event created: {event.get('htmlLink')}")


def main():
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    timezone = 'America/New_York'
    tz = pytz.timezone(timezone)
    datetime_obj = datetime(2023, 8, 19, 15, 0, 0)
    cal = GCalendar(SCOPES)
    events = [{
        "summary": "Test Event",
        "description": "This is a test event",
        "start": {
            "dateTime": datetime_obj.isoformat(),
            "timeZone": timezone,
        },
        "end": {
            "dateTime": (datetime_obj + timedelta(hours=1)).isoformat(),
            "timeZone": timezone,
        },
    },{
        "summary": "Test Event-2",
        "description": "This is a test event",
        "start": {
            "dateTime": datetime_obj.isoformat(),
            "timeZone": timezone,
        },
        "end": {
            "dateTime": (datetime_obj + timedelta(hours=1)).isoformat(),
            "timeZone": timezone,
        },
    },]
    for event in events:
        cal.add_event(event)



if __name__ == '__main__':
    main()