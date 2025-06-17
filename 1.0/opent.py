def read():
	import os

	cwd = os.getcwd()  # Get the current working directory (cwd)
	files = os.listdir(cwd) 
	#print('File in %r %s' % (cwd, files))
	fl = open('data.txt', 'r')
	return fl.read()
	fl.close()
def write(name, data):
	fl = open('data.txt', 'a')
	fl.write(f'"{name}":"{data}"  ')
	fl.close()
def delete():
	fl = open('data.txt', 'w')
	fl.write('')
	fl.close()