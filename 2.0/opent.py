def read_():
	fl = open('main.py', 'r', encoding='utf-8')
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
