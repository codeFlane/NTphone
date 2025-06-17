from musicmanager import opent
from rich import print
print('[magenta]Music manager')
print('[bold black]program for NTphonePy')
#print('[cyan]Укажите вашу директорию:')
#dr = input('musicman>  ')
while True:
	print('[yellow]Введите название файла, или ./exit для выхода.')
	ocmd = input('musicman>  ') 
	if ocmd == './exit':
		break
	else:
		tr = opent.play(ocmd)
		if tr != 1:
			#print('[red]Введёного файла не существует. /')
			print(tr)
		else:
			print(f'[green]Проигрывается файл "{ocmd}"')