def read_(name):
	fl = open(name, 'r', encoding='utf-8')
	return fl.read()
	fl.close()
def write_(name, data):
	fl = open('data.txt', 'a')
	fl.write(f'"{name}":"{data}"  ')
	fl.close()
def delete_(name):
	fl = open(name, 'w')
	fl.write('')
	fl.close()
