def opentxt(name):
	try:
		c = "\ "[0]
		file = open(f'data{c}{name}.txt', 'r', encoding='utf-8')
		return file.read()
	except FileNotFoundError:
		return 'Введёный файл не существует. '
def openpng(name, typ):
	from os import startfile as sf
	try:
		if typ == 'png':
			a = __file__
			a = str(a)
			b = a[0:33]
			c = "\ "[0]
			sf(f'{b}data{c}{name}.png')
			return None
		elif typ == 'jpg':
			a = __file__
			a = str(a)
			b = a[0:33]
			c = "\ "[0]
			sf(f'{b}data{c}{name}.jpg')
			return None
		else:
			return 'Введёный тип файла не существует или его нет в системе NTphonePy. '
	except FileNotFoundError:
		return 'Введёный файл не существует. '