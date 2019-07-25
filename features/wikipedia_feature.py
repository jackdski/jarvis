import wikipedia
from wikipedia import PageError
from colorama import Fore, Back


class Wiki:
	def __init__(self):
		self.valid_inputs = {
			"lookup": 1,
			"whatis": 1,
			"wiki": 1,
			"wikipedia": 1
		}

	@staticmethod
	def look_up(s):
		if any(s) and len(s) > 0:
			try:
				print(Back.BLUE + wikipedia.summary(s))
			except PageError:
				print(Fore.RED + "Page could not be found")
