import sys
from colorama import Fore, Back

from features.calendar_feature import Calendar
from jarvis import Jarvis

features = ["calendar", "weather", "wiki"]

if __name__ == "__main__":
	j = Jarvis()
	while True:
		typed = input("What do you want to do?: ").lower()

		cmd = typed.split(' ')[0]

		if cmd.strip() == 'list':
			j.say("Features available:")
			for feature in features:
				j.say("\t{}".format(feature), Fore.LIGHTBLUE_EX)
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
		elif j.wiki.valid_inputs.get(cmd, 0) > 0:
			s = typed.replace(cmd, '').strip()
			j.say("Wikipedia entry of: {}".format(s))
			j.wiki.look_up(s)
		else:
			print("Command not found")