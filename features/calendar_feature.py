import datetime
import pickle
import os.path
import re
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import pprint

from .utils.calendar_events import CalEvent


class Calendar:
	def __init__(self):
		self.scope = ['https://www.googleapis.com/auth/calendar']
		# SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
		self.valid_inputs = {
			'calendar': 1,
			'cal': 1,
			'calendar list': 2,
			'calendar list ': 2,
			'cal list': 2,
			'cal list ': 2,
			'calendar add': 3,
			'calendar add event': 3,
			'cal add': 3,
			'cal add event': 3,
			'add event': 3,
		}

		self.creds = None

		if os.path.exists('token.pickle'):
			with open('token.pickle', 'rb') as token:
				self.creds = pickle.load(token)

		if not self.creds or not self.creds.valid:
			if self.creds and self.creds.expired and self.creds.refresh_token:
				self.creds.refresh(Request())
			else:
				flow = InstalledAppFlow.from_client_secrets_file('features/utils/credentials.json', self.scope)
				self.creds = flow.run_local_server(port=0)
			with open('token.pickle', 'wb') as token:
				pickle.dump(self.creds, token)

		self.service = build('calendar', 'v3', credentials=self.creds)

		self.now = datetime.datetime.utcnow().isoformat() + 'Z'

	def do_action(self, typed):
		cmd = ''.join([i for i in typed if not i.isdigit()])

		if self.valid_inputs.get(cmd) == 1:
			print("is cal or calendar")
			typed = input("Do you want to:\n1. List upcoming events\n2. Add an event\n")
			if typed.lower().strip() == '1':
				self.list_events(5)
			elif typed.lower().strip() == '2':
				self.add_event()
			else:
				print('Invalid input')
		elif self.valid_inputs.get(cmd) == 2:
			print("Adding event selected")
			# found_number = re.findall(r'\d{2}', typed)
			found_number = ''.join([i for i in typed if i.isdigit()])
			print("found_number: {}".format(found_number))
			if found_number:
				# self.list_events(int(found_number[0]))
				self.list_events(int(found_number))
			else:
				print("Number not found, using default of 5 events")
				self.list_events(5)
		elif self.valid_inputs.get(cmd) == 3:
			self.add_event()
		else:
			print("Did not recognize calendar command")

	def list_events(self, number):
		print('Getting the upcoming {0} events'.format(number))
		events_result = self.service.events().list(calendarId='primary', timeMin=self.now, maxResults=number, singleEvents=True, orderBy='startTime').execute()
		events = events_result.get('items', [])

		if not events:
			print("No upcoming events found")

		# used for debugging
		# pp = pprint.PrettyPrinter(indent=4)
		# pp.pprint(events[0])

		i = 1
		for event in events:
			summary = event['summary']
			start = event['start'].get('dateTime')
			loc = event['location']
			start = start.split('T')
			start[1] = start[1][:-6]
			print("{0}.\t".format(i), summary)
			print("\t", start[0], start[1])

			if '\n' in loc:
				loc = loc.split('\n')
				for j in range(0, len(loc)):
					print("\t", loc[j])
			else:
				print("\t", loc)

			try:
				print(events[0]['description'])
			except KeyError:
				pass
			print('\n')
			i += 1

	def add_event(self):
		new_event = CalEvent()
		print("Creating a new event...")
		new_event.summary = input("Summary: ")
		new_event.location = input("Location: ")
		new_event.description = input("Description: ")
		new_event.start.year = input("Start Year: ")
		new_event.start.month = input("Start Month: ")
		new_event.start.day = input("Start Day: ")
		new_event.start.hour = input("Start Hour: ")
		new_event.start.minute = input("Start Minute: ")
		new_event.end.year = input("End Year: ")
		new_event.end.month = input("End Month: ")
		new_event.end.day = input("End Day: ")
		new_event.end.hour = input("End Hour: ")
		new_event.end.minute = input("End Minute: ")
		new_event.reminders.useDefault = True

		event = new_event.create_event()

		event = self.service.events().insert(calendarId='primary', body=event).execute()
		print('Event created: ', (event.get('htmlLink')))

