def read():
	'''import os

	cwd = os.getcwd()  # Get the current working directory (cwd)
	files = os.listdir(cwd) 
	print('File in %r %s' % (cwd, files))'''
	fl = open('data.txt', 'r')
	return str(fl.read())
	fl.close()
def write(name, data):
	fl = open('data.txt', 'a')
	fl.write(f'"{name}":"{data}"  ')
	fl.close()
def delete():
	fl = open('data.txt', 'w')
	fl.write('')
	fl.close()
def redact(name, ids):
	v = f'{name}: {ids}'
	fl = open('data.txt', 'r')
	if name == 'brouser':
		non = fl.readline()
		a = fl.readline()
		b = fl.readline()
	if name == 'musicman':
		a = fl.readline()
		non = fl.readline()
		b = fl.readline()
	if name == 'lenning':
		a = fl.readline()
		b = fl.readline()
		...
	fl.close()
	fl = open('data.txt', 'w')
	if name == 'brouser':
		fl.write(f'{v}\n')
		fl.write(f'{a}')
		fl.write(f'{b}')
	if name == 'musicman':
		fl.write(f'{a}')
		fl.write(f'{v}\n')
		fl.write(f'{b}')
	if name == 'lenning':
		fl.write(f'{a}')
		fl.write(f'{b}')
		fl.write(f'{v}')