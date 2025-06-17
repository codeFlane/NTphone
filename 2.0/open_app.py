from os import system
def start_app(app, dirr):
	fl = open(f'{dirr}//apps//IMDT.py', 'w+')
	fl.write(f'from {app} import start \n')
	fl.close()

	system('python apps/IMDT.py')
