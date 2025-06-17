def write(name, note):
	fl = open(f'notepad\\{name}.txt', 'a')
	fl.write(f'\n{note}')
	fl.close()
def read(name):
	fl = open(f'notepad\\{name}.txt', 'r')
	ret = fl.read()
	return ret
	fl.close()
def delete(name):
	fl = open(f'notepad\\{name}.txt', 'w')
	fl.write('')
	fl.close()