from time import sleep, time
a = time()
ext = 0
from playsound import playsound
playsound('start.mp3', False)
import opent
from rich import print
from playsound import playsound
from numexpr import evaluate
from rich.progress import track
from notepad import init as notepad
for counter in track(range(90), description='Loading NTphonePy.py...'):
	sleep(0.01)

_dict = opent.read()
if _dict.find('brouser: False') == -1:
	brouser = True
else:
	brouser = False
if _dict.find('musicman: False') == -1:
	musicmanager = True
else:
	musicmanager = False
if _dict.find('lenning: False') == -1:
	lenning = True
else:
	lenning = False
if _dict.find('day_and_time: False') == -1:
	dayandtime = True
else:
	dayandtime = False
b = time()
print(f'[i]{round(b-a, 3)} second.')
print(f'[i]directory [magenta]{__file__}')
print('[cyan]NTphonePy --1.3--')
#print('[blink][red on white]!!!NTphonePy находится в бета тестировании (1.2)')

print('Добро пожаловать!')
print()
while True:
	print('Сиписок:')
	print('[blue]1] Calculator      -calc')
	print('[cyan]2] Secundomer      -seconds')
	print('[bold black]3] Files Manager   -files (перевыпуск in 1.5)')
	print('[green]4] Info            -info')
	print('[magenta]5] Notepad         -note')
	print('[red]6] Store           -store')
	print('[yellow]7] Animation       -anim')
	print('[dim magenta]8][bold] Quit           -exit')
	cmd = input('>')
	if cmd == 'exit':
		break
	elif cmd == 'note':
		print('[yellow]Введите команду: [green](-write -read -delete)')
		acmd = input('>>')
		if acmd == 'write':
			print('[cyan]Введите название заметки:')
			xacmd = input('>>>')
			print('[cyan]Введите запись:')
			facmd = input('>>>')
			notepad.write(xacmd, facmd)
		if acmd == 'read':
			print('[cyan]Введите название заметки:')
			xacmd = input('>>>')
			print(f'[green]{notepad.read(xacmd)}')
		'''if acmd == 'delline':
			print('[cyan]Введите название заметки:')
			xacmd = input('>>>')
			print('[cyan]Введите № строки, которую требуется удалить:')
			facmd = input('>>>')
			print(f'[red]{notepad.deline(xacmd, facmd)}')'''
		if acmd == 'delete':
			print('[red]Вы уверены, что хотите удалить данные заметки? y/n')
			xacmd = input('>>>')
			if xacmd == 'y':
				print('[red]Введите название заметки:')
				facmd = input('>>>>')
				notepad.delete(facmd)
	elif cmd == 'anim':
		print('[green]ANIM: -explos  -granata')
		acmd = input('>>')
		if acmd == 'explos':
			print('anim.explos')
			from animations import explos
			explos.music()
			explos.start()
			explos.music()
			explos.start()
			explos.start()
			explos.music()
			explos.start()
			explos.start()
			explos.music()
			explos.start()
			explos.start()
			explos.music()
			explos.music()
		elif acmd == 'granata':
			print('anim.granata')
			from animations import granata
			granata.start()
			granata.music()
			granata.pos_2()
			granata.pos_3()
			granata.pos_4()
		else:
			print('[red]Введённой анимации не существует. /')
	elif cmd == 'store':
		print('[green on blue]Скачанные')
		_dict = opent.read()
		if _dict.find('brouser: False') == -1:
			brouser = True
		else:
			brouser = False
		if _dict.find('musicman: False') == -1:
			musicmanager = True
		else:
			musicmanager = False
		if _dict.find('lenning: False') == -1:
			lenning = True
		else:
			lenning = False
		if _dict.find('dayandtime: False') == -1:
			dayandtime = True
		else:
			dayandtime = False
		a, b, c, d = 0, 0, 0, 0
		if lenning:
			print()
			print('[cyan]Lenning')
			print('[dim cyan]Быстро измерять число букв в тексте')
			print('[dim cyan]v.1.0 2 791 байт')
			a = 1
		elif musicmanager:
			print()
			print('[magenta]Music manager')
			print('[dim magenta]Мини-проигрыватель')
			print('[dim magenta]v.1.0  2 019 байт')
			b = 1
		elif brouser:
			print()
			print('[green]Brouser')
			print('[dim green]Вводите запрос и переходите на нужный браузер')
			print('[dim green]v.1.0  16 456 байт')
			c = 1
		elif dayandtime:
			print()
			print('[yellow]Day and time')
			print('[dim yellow]Узнайте дату и время через NTphone')
			print('[dim yellow]v.1.0  8 361 байт')
			d = 1
		if not dayandtime and not brouser and not musicmanager and not lenning:
			print('[red]None. У вас нет скачанных приложений. /')
		print()

		print('[green on blue]Можно скачать')
		print('[yellow]new:')
		_dict = opent.read()
		if not lenning or a == 0:
			print()
			print('[cyan]Lenning')
			print('[dim cyan]Быстро измерять число букв в тексте')
			print('[dim cyan]v.1.0  2 791 байт')
		if not musicmanager or b == 0:
			print()
			print('[magenta]Music manager')
			print('[dim magenta]Мини-проигрыватель')
			print('[dim magenta]v.1.0  2 019 байт')
		if not brouser or c == 0:
			print()
			print('[green]Brouser')
			print('[dim green]Вводите запрос и переходите на нужный браузер')
			print('[dim green]v.1.0  16 456 байт')
		if not dayandtime or d == 0:
			print()
			print('[yellow]Day and time')
			print('[dim yellow]Узнайте дату и время через NTphone')
			print('[dim yellow]v.1.0  8 361 байт')
		if dayandtime and brouser and musicmanager and lenning:
			print('[red]None. Вы уже скачали все приложения :Р /')
		print()
		print('[bold black]old:')
		print('[red]None. Старых приложений нет. Всё новое! :) /')
		print()
		acmd = ''
		while acmd != 'phone':
			print('[green]Действия:')
			print('[red]1]Download    -down')
			print('[yellow]2]Read dict   -dict')
			print('[green]3]Delete      -del')
			print('[cyan]4]Open        -open')
			print('[blue]5]Delete all  -delall')
			print('[magenta]6]Exit        -phone')
			print('[dim magenta]7][bold magenta]Exit phone -exitph')
			acmd = input('>>')
			if acmd == 'phone':
				...
			elif acmd == 'down':
				print('[yellow]Выберите приложение, которое нужно установить:')
				print('[green]-brouser     [cyan]-lenning     [magenta]-musicman    [yellow]-dayandtime')
				xacmd = input('>>>')
				if xacmd == 'brouser':
					for counter in track(range(90), description='Download brouser...'):
						sleep(0.007)
					opent.redact('brouser', 'True')
					print('[green]i  brouser.status:1')
				elif xacmd == 'lenning':
					for counter in track(range(90), description='Download lenning...'):
						sleep(0.007)
					opent.redact('lenning', 'True')
					print('[green]i  lenning.status:1')
				elif xacmd == 'musicman':
					for counter in track(range(90), description='Download musicmanager...'):
						sleep(0.007)
					opent.redact('musicman', 'True')
					print('[green]i  music.status:1')
				elif xacmd == 'dayandtime':
					for counter in track(range(90), description='Download dayandtime...'):
						sleep(0.007)
					opent.redact('day_and_time', 'True')
					print('[green]i  day_and_time.status:1')
				else:
					print('[red] Введённого приложения не существует. /')
			elif acmd == 'dict':
				print('[cyan]Содержание текстового документа:')
				print(f'[green]"{opent.read()}"')
			elif acmd == 'del':
				print('[yellow]Выберите приложение, которое нужно удалить:')
				print('[green]-brouser     [cyan]-lenning     [magenta]-musicman   [yellow]-dayandtime')
				xacmd = input('>>>')
				if xacmd == 'brouser':
					if brouser:
						for counter in track(range(90), description='Delete brouser...'):
							sleep(0.006)
						opent.redact('brouser', 'False')
						print('[green]i  brouser.status:0')
					else:
						print('[red]brouser не установлен. /')
				if xacmd == 'musicman':
					if musicmanager:
						for counter in track(range(90), description='Delete musicmanager...'):
							sleep(0.006)
						opent.redact('musicman', 'False')
						print('[green]i  music.status:0')
					else:
						print('[red]musicmanager не установлен. /')  
				if xacmd == 'lenning':
					if lenning:
						for counter in track(range(90), description='Delete lenning...'):
							sleep(0.006)
						opent.redact('lenning', 'False')
						print('[green]i  mlenning.status:0')
					else:
						print('[red]lenning не установлен. /')
				if xacmd == 'dayandtime':
					if dayandtime:
						for counter in track(range(90), description='Delete dayandtime...'):
								sleep(0.001)
						opent.redact('day_and_time', 'False')
						print('[green]i  day_and_time.status:0')
					else:
						print('[red]day and time не установлен. /')
				
			elif acmd == 'exitph':
				ext = 1
				break  
			elif acmd == 'open':
				print('[green on blue]Выберите приложение, которое требуется открыть:')
				print('[green]-brouser     [cyan]-lenning     [magenta]-musicman    [yellow]-dayandtime')
				xacmd = input('>>>')

				_dict = opent.read()
				if _dict.find('brouser: False') == -1:
					brouser = True
				else:
					brouser = False
				if _dict.find('musicman: False') == -1:
					musicmanager = True
				else:
					musicmanager = False
				if _dict.find('lenning: False') == -1:
					lenning = True
				else:
					lenning = False
				if _dict.find('day_and_time: False') == -1:
					dayandtime = True
				else:
					dayandtime = False

				if xacmd == 'brouser':
					if brouser:
						from brouser import init
					else:
						print('[red]brouser не установлен. /')
				if xacmd == 'lenning':
					if lenning:
						from lenning import init
					else:
						print('[red]lenning не установлен. /')
				if xacmd == 'musicman':
					if musicmanager:
						from musicmanager import init
					else:
						print('[red]musicmanager не установлен. /')		
				if xacmd == 'dayandtime':
					if dayandtime:
						from day_and_time import init
					else:
						print('[red]day and time не установлен. /')

			elif acmd == 'delall':
				_dict = opent.read()
				if _dict.find('brouser: False') == -1:
					brouser = True
				else:
					brouser = False
				if _dict.find('musicman: False') == -1:
					musicmanager = True
				else:
					musicmanager = False
				if _dict.find('lenning: False') == -1:
					lenning = True
				else:
					lenning = False
				if _dict.find('day_and_time: False') == -1:
					dayandtime = True
				else:
					dayandtime = False

				print('[red]Вы уверены, что хотите удалить все приложения? y/n')
				xacmd = input('>>>')
				if xacmd == 'y':
					if brouser:
						for counter in track(range(90), description='Delete brouser...'):
							sleep(0.01)
						opent.redact('brouser', 'False')
						print('[green]i  brouser.status:0')
					else:
						print('[red]brouser не установлен. /')
					if musicmanager:
						for counter in track(range(90), description='Delete musicmanager...'):
							sleep(0.01)
						opent.redact('musicman', 'False')
						print('[green]i  music.status:0')
					else:
						print('[red]musicmanager не установлен. /') 
					if lenning:
						for counter in track(range(90), description='Delete lenning...'):
							sleep(0.01)
						opent.redact('lenning', 'False')
						print('[green]i  lenning.status:0')
					else:
						print('[red]lenning не установлен. /')
					if dayandtime:
						for counter in track(range(90), description='Delete dayandtime...'):
							sleep(0.01)
						opent.redact('day_and_time', 'False')
						print('[green]i  dayandtime.status:0')
					else:
						print('[red]day and time не установлен. /')
	elif cmd == 'calc':
		print('[cyan]Действия:')
		print('[red]1] numexpr  -nums')
		print('[green]2] /+ost    -"/"')
		print('[magenta]3] classes  -clas')
		acmd = input('>>')
		if acmd == 'clas':
			print('[red on white]!! BETA-TEST functional !!')
			print('[bold black]Тест закончится к версии 1.3')
			from troecrat import *
			print('Введите число (до 999 биллионов):')
			xacmd = input('>>>')
			if len(xacmd) < 4:
				print(xacmd)
			elif len(xacmd) < 7:
				xacmd = xacmd + '                '
				if not troecrat(xacmd):
					if for_troecrat(xacmd) == 1:
						print(f'{xacmd[0]} thousand {xacmd[1]}{xacmd[2]}{xacmd[3]}')
					if for_troecrat(xacmd) == 2:
						print(f'{xacmd[0]}{xacmd[1]} thousand {xacmd[2]}{xacmd[3]}{xacmd[4]}')
				else:
					print(f'{xacmd[0]}{xacmd[1]}{xacmd[2]} thousand {xacmd[3]}{xacmd[4]}{xacmd[5]}')
				print('troecrat (0,1):', troecrat(xacmd))
				print('for_troecrat (0,2):', for_troecrat(xacmd))	
				print('len:', nlen(xacmd))	

			elif len(xacmd) < 10:
				xacmd = xacmd + '                '
				if not troecrat(xacmd):
					if for_troecrat(xacmd) == 1:
						print(f'{xacmd[0]} million {xacmd[1]}{xacmd[2]}{xacmd[3]} thousand {xacmd[4]}{xacmd[5]}{xacmd[6]}')
					if for_troecrat(xacmd) == 2:
						print(f'{xacmd[0]}{xacmd[1]} million {xacmd[2]}{xacmd[3]}{xacmd[4]} thousand {xacmd[5]}{xacmd[6]}{xacmd[7]}')
				else:	
					print(f'{xacmd[0]}{xacmd[1]}{xacmd[2]} million {xacmd[3]}{xacmd[4]}{xacmd[5]} thousand {xacmd[6]}{xacmd[7]}{xacmd[8]}')
				print('troecrat (0,1):', troecrat(xacmd))
				print('for_troecrat (0,2):', for_troecrat(xacmd))	
				print('len:', nlen(xacmd))	
			elif len(xacmd) < 13:
				xacmd = xacmd + '                '
				if not troecrat(xacmd):
					if for_troecrat(xacmd) == 1:
						print(f'{xacmd[0]} milliard {xacmd[1]}{xacmd[2]}{xacmd[3]} million {xacmd[4]}{xacmd[5]}{xacmd[6]} thousand {xacmd[7]}{xacmd[8]}{xacmd[9]}')
					if for_troecrat(xacmd) == 2:
						print(f'{xacmd[0]}{xacmd[1]} milliard {xacmd[2]}{xacmd[3]}{xacmd[4]} million {xacmd[5]}{xacmd[6]}{xacmd[7]} thousand {xacmd[8]}{xacmd[9]}{xacmd[10]}')
				else:	
					print(f'{xacmd[0]}{xacmd[1]}{xacmd[2]} milliard {xacmd[3]}{xacmd[4]}{xacmd[5]} million {xacmd[6]}{xacmd[7]}{xacmd[8]} thousand {xacmd[9]}{xacmd[10]}{xacmd[11]}')
					
				print('troecrat (0,1):', troecrat(xacmd))
				print('for_troecrat (0,2):', for_troecrat(xacmd))	
				print('len:', nlen(xacmd))
			elif len(xacmd) < 16:
				xacmd = xacmd + '                   '
				if not troecrat(xacmd):
					if for_troecrat(xacmd) == 1:
						print(f'{xacmd[0]} billion {xacmd[1]}{xacmd[2]}{xacmd[3]} milliard {xacmd[4]}{xacmd[5]}{xacmd[6]} million {xacmd[7]}{xacmd[8]}{xacmd[9]} thousand {xacmd[8]}{xacmd[9]}{xacmd[10]}')
					if for_troecrat(xacmd) == 2:
						print(f'{xacmd[0]}{xacmd[1]} billion {xacmd[2]}{xacmd[3]}{xacmd[4]} milliard {xacmd[5]}{xacmd[6]}{xacmd[7]} million {xacmd[8]}{xacmd[9]}{xacmd[10]} thousand {xacmd[11]}{xacmd[12]}{xacmd[13]}')
				else:	
					print(f'{xacmd[0]}{xacmd[1]}{xacmd[2]} billion {xacmd[3]}{xacmd[4]}{xacmd[5]} milliard {xacmd[6]}{xacmd[7]}{xacmd[8]} million {xacmd[9]}{xacmd[10]}{xacmd[11]} thousand {xacmd[12]}{xacmd[13]}{xacmd[14]}')
			else:
				print(f'[red]Len error code:{len(xacmd)} /')	
			print('troecrat (0,1):', troecrat(xacmd))
			print('for_troecrat (0,2):', for_troecrat(xacmd))	
			print('len:', nlen(xacmd))	
			if for_troecrat(xacmd) == 0 and troecrat == 0:
				print('[red]For_troecrat error code:0 /')	
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
			if dt1 == 0:
				ans2 = dt2
			num = ans * dt2
			print(f'[green]answer:{ans} (ost. {ans2}) [yellow]Старт-число: {num}')
	elif ext:
		break
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
	    #elif cmd == 'files':
		#import filesmanager as fm
		#print('[magenta]Введите тип файла: txt/png/jpg:')
		#tpe = input('>>')
		#print('[blue]Введите название файла:')
		#nm = input('>>')
		#print('[cyan]Введите директорию файла:')
		#dr = input('>>')
		#if tpe == 'txt':
			#if fm.opentxt(nm) != 'Введёный файл не существует. /':
			#	print(f'"{fm.opentxt(nm)}"')
			#else:
			#	print('[red]Введёный файл не существует. /')
		#else:
			#eror = fm.openpng(nm, tpe, dr)
			#if eror != None:
			#	print(f'[red]{eror}')'''
	elif cmd == 'info':
		print('[green on white]NTphonePy 1.3 _  482 строк  _ дата выхода: 30.10.22 _ (init:18 153 байт  filesmanger: None  opent: 1 027 байт  animations: 342 343 байт  dop_data(store): 32 377 байт) ')
		print('[blue]Вес NTphonePy1.3: 688 719 байт')
		print('[yellow]* "/" означает конец вывода ошибки')
		print('[blue]Скоро в функционале: Notepad, выход из бета-теста ".calc/clas')
	else:
		print('[red] Введённой команды не существует. /')
print('Press Enter to continue...')
input('')