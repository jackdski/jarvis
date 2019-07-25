# features
from features.calendar_feature import Calendar
from features.weather import Weather
from features.wikipedia_feature import Wiki

from colorama import init, Fore, Back, Style


class Jarvis:
	def __init__(self):
		self.cal = Calendar()
		self.weather = Weather()
		self.wiki = Wiki()
		init(autoreset=True)
		print(Fore.CYAN + "J A R V I S")

	@staticmethod
	def say(s, color=Fore.CYAN):
		print(color + s)
