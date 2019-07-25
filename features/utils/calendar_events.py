class CalEvent(object):
	"""docstring for CalEvent"""
	def __init__(self):
		self.summary = None
		self.location = None
		self.description = None
		self.start = EventTime()
		self.end = EventTime()
		self.reminders = EventReminders()

	def help(self):
		pass

	def create_event(self):
		event_str = dict()
		event_str['summary'] = self.format_summary()
		event_str['location'] = self.format_location()
		event_str['description'] = self.format_description()
		event_str['start'] = self.format_start()
		event_str['end'] = self.format_end()
		event_str['reminders'] = self.format_reminders()

		return event_str

	def format_summary(self):
		if isinstance(self.summary, str):
			return self.summary
		else:
			raise ValueError("Summary is empty, add a summary and try again")

	def format_location(self):
		if isinstance(self.location, str):
			return self.location

	def format_description(self):
		if isinstance(self.description, str):
			return self.description

	def format_start(self):
		# time_str = """\'start\': {{\n\'dateTime\': \'"""
		datetime_str = str()

		# format year
		if isinstance(self.start.year, str) and len(self.start.year) == 4:
			datetime_str += str(self.start.year) + '-'
		else:
			if not isinstance(self.start.year, str):
				raise ValueError("Year input is incorrect")
			if len(self.start.year) != 4:
				raise ValueError("Enter a valid year value")

		# format month
		if isinstance(self.start.month, str):
			if len(self.start.month) == 1:
				datetime_str += """0{}""".format(str(self.start.month))
			elif len(self.start.month) == 2:
				datetime_str += str(self.start.month)
			datetime_str += '-'
		else:
			raise ValueError("Month input is incorrect")

		# format day
		if isinstance(self.start.day, str):
			if len(self.start.day) == 1:
				datetime_str += """0{}""".format(str(self.start.day))
			elif len(self.start.day) == 2:
				datetime_str += str(self.start.day)
			datetime_str += 'T'
		else:
			raise ValueError("Day input is incorrect")

		""" at this postr 'time_string' should be along the lines of:
			\'start\': {\n\'dateTime\':\'2019-01-01T """

		# format hours
		if isinstance(self.start.hour, str):
			if len(self.start.hour) == 1:
				datetime_str += """0{}:""".format(self.start.hour)
			elif len(self.start.hour) == 2:
				datetime_str += """{}:""".format(self.start.hour)
		else:
			print(type(self.start.hour))
			raise ValueError("Hour input is incorrect")

		# format minutes
		if isinstance(self.start.minute, str):
			if len(self.start.minute) == 1:
				datetime_str += """0{}:00""".format(self.start.minute)
			elif len(self.start.minute) == 2:
				datetime_str += """{}:00""".format(self.start.minute)
		elif self.end.minute is None:
			datetime_str += """00:00"""
		else:
			print(type(self.start.minute))
			raise ValueError("Minute input is incorrect")

		time_str = dict()

		time_str['dateTime'] = datetime_str

		# format timezone
		if isinstance(self.start.time_zone, str) and '/' in self.start.time_zone:
			# datetime_str += """\'timeZone\': \'{}\',\n}},""".format(self.start.time_zone)
			time_str['timeZone'] = self.start.time_zone
		else:
			raise ValueError("Time Zone input is incorrect, add a time zone and try again")

		return time_str

	def format_end(self):
		# time_str = """\'end\': {{\n\'dateTime\': \'"""
		datetime_str = str()

		# format year
		if isinstance(self.end.year, str) and len(self.end.year) == 4:
			datetime_str += str(self.end.year) + '-'
		else:
			if not isinstance(self.end.year, str):
				raise ValueError("Year input is incorrect")
			if len(self.end.year) != 4:
				raise ValueError("Enter a valid year value")

		# format month
		if isinstance(self.end.month, str):
			if len(self.end.month) == 1:
				datetime_str += """0{}""".format(str(self.end.month))
			elif len(self.end.month) == 2:
				datetime_str += str(self.end.month)
			datetime_str += '-'
		else:
			raise ValueError("Month input is incorrect")

		# format day
		if isinstance(self.end.day, str):
			datetime_str += str(self.end.day)
			datetime_str += 'T'
		else:
			raise ValueError("Day input is incorrect")

		""" at this postr 'time_string' should be along the lines of:
			\'end\': {\n\'dateTime\':\'2019-01-01T """

		# format hours
		if isinstance(self.end.hour, str):
			if len(self.end.hour) == 1:
				datetime_str += """0{}:""".format(self.end.hour)
			elif len(self.end.hour) == 2:
				datetime_str += """{}:""".format(self.end.hour)
		else:
			print(type(self.end.hour))
			raise ValueError("Hour input is incorrect")

		# format minutes
		if isinstance(self.end.minute, str):
			if len(self.end.minute) == 1:
				datetime_str += """0{}:00""".format(self.end.minute)
			elif len(self.end.minute) == 2:
				datetime_str += """{}:00""".format(self.end.minute)
		elif self.end.minute is None:
			datetime_str += """00:00"""
		else:
			print(type(self.end.minute))
			raise ValueError("Minute input is incorrect")

		time_str = dict()

		time_str['dateTime'] = datetime_str

		# format timezone
		if isinstance(self.end.time_zone, str) and '/' in self.end.time_zone:
			# datetime_str += """\'timeZone\': \'{}\',\n}},""".format(self.end.time_zone)
			time_str['timeZone'] = self.end.time_zone
		else:
			raise ValueError("Time Zone input is incorrect, add a time zone and try again")

		return time_str

	def format_reminders(self):
		# reminder_str = """\'reminders\': {\n\'useDefault\': """
		reminder_str = dict()
		if self.reminders.useDefault:
			reminder_str['useDefault'] = True
		elif not self.reminders.useDefault:
			reminder_str['overrides'] = list(dict[('method', 'popup'), ('minutes', 10)])
			# reminder_str += "False,\n\'overrides\': [\n{\'method\': \'popup\', \'minutes\': 10}},\n],"
		# reminder_str += """'}},"""

		return reminder_str

class EventTime(object):
	def __init__(self, year=None, month=None, day=None, hour=None, minute=None, time_zone='Europe/Berlin'):
		self.year = year,
		self.month = month
		self.day = day
		self.hour = hour
		self.minute = minute
		self.time_zone = time_zone


class EventReminders(object):
	def __init__(self, use_default=True, overrides=None):
		self.useDefault = use_default
		self.overrides = overrides
