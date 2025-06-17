def play(name):
	try:
		dr = __file__.find('opent.py')
		dri = __file__[0:dr]
		from time import sleep
		from playsound import playsound
		sleep(0.01)
		playsound(f'{dri}\\{name}')
	except Exception as e:
		return e