from time import sleep, time
a = time()
import opent
from rich import print
from playsound import playsound
from numexpr import evaluate
from rich.progress import track
for counter in track(range(90), description='Loading NTphonePy.py...'):
	sleep(0.001)

b = time()
print(f'[i]{round(b-a, 3)} second.')
print(f'[i]directory [magenta]{__file__}')
print('[cyan]NTphonePy --1.0--')
#print('[blink][red on white]!!!NTphonePy находится в бета тестировании (0.1)')

if opent.read() == '':
	print('!Введите ваше имя: ... \a')
	name = input('>')
	opent.write('name', name)
	print(f'[green]Success! *write name:{name}* result: -->data.txt<--')
print('Добро пожаловать!')
print()
while True:
	print('Сиписок:')
	print('[red]1] Calculator    -calc')
	print('[yellow]2] Secundomer    -seconds')
	print('[green]3] Files Manager -files')
	print('[blue]4] Info          -info')
	print('[magenta]5] Quit          -exit')
	print('[bold black]6] Store         -store (in 1.1)')
	cmd = input('>')
	if cmd == 'exit':
		break
	if cmd == 'calc':
		print('[cyan]Действия:')
		print('[red]1] numexpr  -nums')
		print('[magenta]2] /+ost    -"/"')
		acmd = input('>>')
		if acmd == 'nums':
			print('[green]Введите пример:')
			dt1 = input('>>>')
			ans = evaluate(dt1)
			print(f'[green]answer:{ans}')
		if acmd == '/':
			print('Введите 1 число:')
			dt1 = int(input('>>>'))
			print('Введите 2 число:')
			dt2 = int(input('>>>'))
			ans = dt1 // dt2
			ans2 = dt1 % dt2
			num = ans - ans2 - ans2
			print(f'[green]answer:{ans} (ost. {ans2}) [yellow]Старт-число: {num}')
	elif cmd == 'seconds':
		print('[yellow]Введите, до скольки округлить числа:')
		num = int(input('>>'))
		print('[blue on green]Нажмите Enter для старта:')
		input('>>')
		a = time()
		print('[magenta on cyan]Нажмите Enter для остановки:')
		input('>>')
		b = time()
		print(f'[yellow]Время от начала до конца: {round(b-a, num)}')
	elif cmd == 'files':
		import filesmanager as fm
		print('[magenta]Введите тип файла: txt/png/jpg:')
		tpe = input('>>')
		print('[blue]Введите название файла:')
		nm = input('>>')
		if tpe == 'txt':
			if fm.opentxt(nm) != 'Введёный файл не существует. ':
				print(f'"{fm.opentxt(nm)}"')
			else:
				print('[red]Введёный файл не существует. [71] /')
		else:
			eror = fm.openpng(nm, tpe)
			if eror != None:
				print(f'[red]{eror} NTphonePy1.0 [76]. /')
	elif cmd == 'info':
		print('[green on white]NTphonePy 1.0 _  86 строк  _ дата выхода: 21.10.22 _  3 974 байт (init:3 144 байт  filesmanger: 718 байт  opent: 389 байт  dop_data: 112 байт)')
		print('[yellow]* "/" означает конец вывода ошибки')
		print('[blue]Скоро в функционале: Store, немного другой FilesManager (1.1)')
	else:
		print('[red] Введённой команды не существует. /')
print('Press Enter to continue...')
input('')