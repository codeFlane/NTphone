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
		c = fl.readline()
		d = fl.readline()
	if name == 'musicman':
		a = fl.readline()
		non = fl.readline()
		b = fl.readline()
		c = fl.readline()
		d = fl.readline()
	if name == 'lenning':
		a = fl.readline()
		b = fl.readline()
		non = fl.readline()
		c = fl.readline()
		d = fl.readline()
	if name == 'day_and_time':
		a = fl.readline()
		b = fl.readline()
		c = fl.readline()
		non = fl.readline()
		d = fl.readline()
	if name == 'os':
		a = fl.readline()
		b = fl.readline()
		c = fl.readline()
		d = fl.readline()
	fl.close()
	fl = open('data.txt', 'w')
	if name == 'brouser':
		fl.write(f'{v}\n')
		fl.write(f'{a}')
		fl.write(f'{b}')
		fl.write(f'{c}')
		fl.write(f'{d}')
	if name == 'musicman':
		fl.write(f'{a}')
		fl.write(f'{v}\n')
		fl.write(f'{b}')
		fl.write(f'{c}')
		fl.write(f'{d}')
	if name == 'lenning':
		fl.write(f'{a}')
		fl.write(f'{b}')
		fl.write(f'{v}\n')
		fl.write(f'{c}')
		fl.write(f'{d}')
	if name == 'day_and_time':
		fl.write(f'{a}')
		fl.write(f'{b}')
		fl.write(f'{c}')
		fl.write(f'{v}\n')
		fl.write(f'{d}')
	if name == 'os':
		fl.write(f'{a}')
		fl.write(f'{b}')
		fl.write(f'{c}')
		fl.write(f'{d}')
		fl.write(f'{v}')