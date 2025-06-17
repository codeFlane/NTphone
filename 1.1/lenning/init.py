from rich import print
from lenning import opent
print('[green]Lenning')
print('[bold black]program for NTphonePy')
while True:
	print('[cyan]Введите текст, чтобы узнать, сколько в нем символов (или ./file, чтобы открыть файл)')
	print('[bold black]#./exit - выход')
	ocmd = input('lenning>  ')
	if ocmd == './exit':
		break
	if ocmd == './file':
		print('[magenta]Введите название файла: [cyan](без .txt) [blue](file должен находится в этой директории)')
		xocmd = input('lenning>>  ')
		try:
			print(f'[green]len: {len(opent.read(xocmd))} symbols.')
		except FileNotFoundError:
			print('[red]ыыыы... файла не существует. /')
	else:
		print(f'[green]len: {len(ocmd)} symbols.')