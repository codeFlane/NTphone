from rich import print
from os import mkdir, remove, rmdir, listdir
def NTPhoneObject076():
	print('[red](По техническим причинам акценты и темы стандартные)')
	print('[yellow]Введите номер команды:')
	print('[bold yellow]1: Cоздать файл')
	print('[bold yellow]2: Создать папку')
	print('[bold yellow]3: Удалить файл')
	print('[bold yellow]4: Удалить пустую папку')
	print('[bold yellow]5: Просмотреть файлы и папки в директории')
	command1 = input('>>')
	if command1 == '1':
		print('[cyan]Введите директорию с названием файла:')
		command2 = input('>>>')
		fl = open(command2, 'w+')
		fl.close()
		print('[green]Файл создан!')
	elif command1 == '2':
		print('[cyan]Введите директорию с названием папки:')
		command2 = input('>>>')
		mkdir(command2)
		print('[green]Папка создана!')
	elif command1 == '3':
		print('[cyan]Введите директорию с названием файла:')
		command2 = input('>>>')
		remove(command2)
		print('[green]Файл удален!')
	elif command1 == '4':
		print('[cyan]Введите директорию с названием папки:')
		command2 = input('>>>')
		rmdir(command2)
		print('[green]Папка удалена!')
	elif command1 == '5':
		print('[cyan]Введите директорию:')
		command2 = input('>>>')
		print(listdir(command2))
	else:
		print('[red]Введена неверная команда in line 38 [MODULE] #001')