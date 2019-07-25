import requests
import json


class Weather:
	def __init__(self):
		self.valid_inputs = {'weather': 1}
		self.url = "http://api.openweathermap.org/data/2.5/forecast?q="
		self.url_mode_key = "&mode=json&units=metric&APPID=95f93c13ee33a59d9818e3e9c321791b"
		self.location = None
		self.temperature_metric = 'fahrenheit'

		# getting settings
		try:
			with open('features/utils/settings.txt', 'r') as f:
				line = f.readline()
				while line:
					if 'location=' in line:
						loc = line.strip('location=')
						if any(loc):
							loc = loc.replace('\n', '')
							# print("Location is: ", loc)
							self.location = loc.replace(' ', '+')

					if 'temperature=' in line:
						t = line.strip('temperature=')
						if any(t):
							# print("Temperature metric: ", t)
							self.temperature_metric = t.strip()
					line = f.readline()
		except FileNotFoundError('settings.txt not found'):
			pass

	def format_url(self, city, country):
		return (self.url + "{0},{1}".format(city, country) + self.url_mode_key).strip('\n')

	def get_weather(self, location='settings'):
		if location == 'settings':
			location = self.location.replace(' ', '+')
			location = location.split(',')
		else:
			location = location.strip('\n')
			location = location.replace(' ', '+')
			location = location.split(',')

		url = str(self.format_url(location[0], location[1]))
		location = (location[0] + ',' + location[1]).replace('+', ' ')
		weather_data = requests.get(url)
		weather_data = json.loads(weather_data.text)

		max_temps = []
		min_temps = []

		try:
			for i in range(0, 5):
				max_temps.append(weather_data['list'][i]['main']['temp_max'])
				min_temps.append(weather_data['list'][i]['main']['temp_min'])

			if self.temperature_metric == "fahrenheit" or self.temperature_metric == 'f':
				print("     ", location)
				print("High: {0}\tLow: {1}".format(self.c_to_f(max(max_temps)), self.c_to_f(min(min_temps))))
			elif self.temperature_metric == 'celsius' or self.temperature_metric == 'c' or not any(
					self.temperature_metric):
				print("   ", location)
				print("High: {0}\tLow: {1}".format(max(max_temps), min(min_temps)))
		except KeyError:
			print("Could not get weather data for {}. Try a nearby place?".format(location))

	@staticmethod
	def c_to_f(temperature):
		return ((temperature * 9) / 5) + 32

