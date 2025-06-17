def opentxt(name, direct):
	try:
		c = "\ "[0]
		file = open(f'{direct}{c}{name}.txt', 'r', encoding='utf-8')
		return file.read()
	except FileNotFoundError:
		return 'Введёный файл не существует. /'
def openpng(name, direct, typ):
	from os import startfile as sf
	try:
		if typ == 'png':
			c = "\ "[0]
			sf(f'{direct}{c}{name}.png')
			return None
		elif typ == 'jpg':
			c = "\ "[0]
			sf(f'{direct}{c}{name}.jpg')
			return None
		elif typ == 'gif':
			c = "\ "[0]
			sf(f'{direct}{c}{name}.gif')
			return None
		else:
			return 'Введёный тип файла не существует или его нет в системе NTphonePy. /'
	except FileNotFoundError:
		return 'Введёный файл не существует. /'