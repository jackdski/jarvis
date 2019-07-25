import sys

from features.calendar_feature import Calendar
from jarvis import Jarvis

features = ["calendar", "weather"]

if __name__ == "__main__":
	j = Jarvis()
	while True:
		typed = input("What do you want to do?: ").lower()

		cmd = typed.split(' ')[0]

		if cmd.strip() == 'list':
			j.say("Features available:")
			j.say(', '.join(features))
			j.say('')
		elif cmd.strip() == 'exit' or cmd.strip() == 'close':
			j.say("G O O D B Y E")
			exit(0)
		elif j.cal.valid_inputs.get(cmd, 0) > 0:
			action = j.cal.do_action(typed)
		elif j.weather.valid_inputs.get(cmd, 0) > 0:
			if any(typed.strip('weather ')):
				j.weather.get_weather(typed.replace('weather ', ''))
			else:
				j.weather.get_weather()
		else:
			print("Command not found")