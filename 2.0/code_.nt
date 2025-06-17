try:
	from rich import print
	#modules
	#from time import sleep
	#from playsound import playsound
	#venom
	from data.NTPhoneModule004 import NTPhoneObject076
	from os import listdir, remove, rmdir, system, mkdir
	from time import time
	from pyautogui import alert
	from opent import read_
	#variables
	
	dirr = __file__[0:__file__.find('main.py')]
	apps = listdir(dirr + '\\apps\\')
	
	#tema
	fl = open(f'{dirr}data\\tema.nt', 'r')
	tema = fl.read()
	fl.close()

	#update message (true/false)
	fl = open('data\\upd-msg.nt', 'r')
	upd_msg = fl.read()
	fl.close()

	#accents
	fl = open('data\\accent.nt', 'r')
	accent = fl.read()
	fl.close()
	fl = open('data\\accent2.nt', 'r')
	accent2 = fl.read()
	fl.close()
	fl = open('data\\accent3.nt', 'r')
	accent3 = fl.read()
	fl.close()
	fl = open('data\\accent4.nt', 'r')
	accent4 = fl.read()
	fl.close()
	
	#errors
	class ExitUserError(Exception):
		pass

	# if update   
	def upd():
		fl1 = read_()
		fl2 = open('code_.nt', 'r', encoding='utf-8') 
		if fl1 != fl2.read():
			fl2.close()
			fl3 = open('code_.nt', 'w', encoding='utf-8')
			fl3.write(fl1)
			fl3.close()
			if upd_msg == True:    
				alert('NTphone был изменен! Перезапустите телефон.')
				print(upd_msg)

	#comand of class
	class Comand:
		def calculator(self):
			print(f'[{accent} {tema}]Введите тип калькулятора:')
			print(f'[bold {accent} {tema}]1: Калькулятор в одну строку')
			print(f'[bold {accent} {tema}]2: Обычный калькулятор')
			print(f'[bold {accent} {tema}]3: Калькулятор деления с остатком')
			command = input('>>')
			upd()
			if command == '1':
				print(f'[{accent2} {tema}]Введите пример целиком:')
				print('Ответ: ', eval(input('>>>')))
			elif command == '2':
				print(f'[{accent2} {tema}]Введите пример:')
				command = input('>>>')
				upd()
				try:
					print(eval(command))
				except ZeroDivisionError:
					print(f'[red {tema}]Деление на ноль in line 76 #002')
			elif command == '3':
				try:
					print(f'[{accent2} {tema}]Введите 1 число')
					command = int(input('>>>'))
					print(f'[{accent2} {tema}]Введите 2 число')
					command1 = int(input('>>>'))
					if command1 == 0:
						print(f'[red {tema}]Деление на ноль in line 84 #002')
					else:
						ans = command // command1
						ans2 = command % command1
						num = ans * command1
						upd()
						print(f'[{accent} {tema}]Ответ: {ans}')
						print(f'[{accent} {tema}]Остаток: {ans2}')
						print(f'[{accent3} {tema}]Старт-число: {num}')
				except TypeError:
					print(f'[red {tema}]Ошибка в значениях переменной in line 94 #005')
		def secundomer(self):
			print(f'[{accent} {tema}]Введите, до скольки округлить числа:')
			num = int(input('>>'))
			print(f'[{accent2} {tema}]Нажмите Enter для старта:')
			input('>>')
			a = time()
			upd()
			print(f'[{accent2} {tema}]Нажмите Enter для остановки:')
			input('>>')
			b = time()
			print(f'[{accent3} {tema}]Время от начала до конца: {round(b-a, num)}')
		def file_manager(self):
			NTPhoneObject076()
		def settings(self,tema):
			print(f'[{accent} {tema}]Введите номер команды:')
			print(f'[bold {accent} {tema}]1: Изменить тему')
			print(f'[bold {accent} {tema}]2: Изменить цветовые акценты')
			print(f'[bold {accent} {tema}]3: Сброс до заводских настроек')
			print(f'[bold {accent} {tema}]4: Параметры уведомлений об изенении файла запуска')
			print(f'[bold {accent} {tema}]5: Информация о разработчике')
			print(f'[bold {accent} {tema}]6: Информация о версии телефона')
			print(f'[bold {accent} {tema}]7: Удалить NTphone')
			command = input('>>')
			if command == '1':
				print(f'[{accent2} {tema}]Выберите тему:')
				print(f'[bold {accent2} {tema}]1: Светлая')
				print(f'[bold {accent2} {tema}]2: Тёмная (стандарт)')
				print(f'[bold {accent2} {tema}]3: Выйти')
				command1 = input('>>>')
				if command1 == '1':
					print(f'[{accent3} {tema}]Установлена светлая тема.')
					print(f'[red {tema}]Внимание: Не устанавливайте белые акценты.')
					tema = 'on white'
					fl = open(f'{dirr}//data//tema.nt', 'w')
					fl.write('on white')
					fl.close()
					print(f'[{accent3} {tema}]Настройки успешно изменены.')
				elif command1 == '2':
					print(f'[{accent3} {tema}]Установлена тёмная тема.')
					tema = ''
					fl = open(f'{dirr}//data//tema.nt', 'w')
					fl.write('')
					fl.close()
				elif command1 == '3':
					pass
				else:
					print(f'[red {tema}]Неверная команда in line 141 #001')
			elif command == '2':
				print(f'[{accent} {tema}]Цветовые акценты:')
				print(f'[bold {accent2} {tema}]Акцент 1: "{accent}"')
				print(f'[bold {accent2} {tema}]Акцент 2: "{accent2}"')
				print(f'[bold {accent2} {tema}]Акцент 3: "{accent3}"')
				print(f'[bold {accent2} {tema}]Акцент 4: "{accent4}"')
				print()
				print(f'[{accent} {tema}] Выберите акцент, который вы хотите изменить:')
				print(f'[bold {accent} {tema}]1: Акцент 1, 2: Акцент 2, 3: Акцент 3, 4: Акцент 4, 5: Выйти')
				command1 = input('>>>')
				print(f'[{accent3} {tema}]Выберите номер цвета для акцента:')
				print(f'[bold {accent3} {tema}]1: red, 2: yellow, 3: green, 4: cyan, ')
				print(f'[bold {accent3} {tema}]5: blue, 6: magenta, 7: black, 8: white, 9: Выйти')
				command2 = input('>>>>')
				if command1 == '1':
					fl = open(f'{dirr}//data//accent.nt', 'w')
				elif command1 == '2':
					fl = open(f'{dirr}//data//accent2.nt', 'w')
				elif command1 == '3':
					fl = open(f'{dirr}//data//accent3.nt', 'w')
				elif command1 == '4':
					fl = open(f'{dirr}//data//accent4.nt', 'w')
				elif command1 == '5':
					pass
				else:
					print(f'[red {tema}]Неверная команда in line 167 #001')
					fl = ''
				if fl != '':
					if command2 == '1':
						fl.write('red')
						print(f'[{accent3} {tema}]Настройки успешно изменены.')
					elif command2 == '2':
						fl.write('yellow')
						print(f'[{accent3} {tema}]Настройки успешно изменены.')
					elif command2 == '3':
						fl.write('green')
						print(f'[{accent3} {tema}]Настройки успешно изменены.')
					elif command2 == '4':
						fl.write('cyan')
						print(f'[{accent3} {tema}]Настройки успешно изменены.')
					elif command2 == '5':
						fl.write('blue')
						print(f'[{accent3} {tema}]Настройки успешно изменены.')
					elif command2 == '6':
						fl.write('magenta')
						print(f'[{accent3} {tema}]Настройки успешно изменены.')
					elif command2 == '7':
						fl.write('black')
						print(f'[{accent3} {tema}]Настройки успешно изменены.')
					elif command2 == '8':
						fl.write('white')
						print(f'[{accent3} {tema}]Настройки успешно изменены.')
					elif command2 == '9':
						pass
					else:
						print(f'[red {tema}]Неверная команда in line 197 #001')
					fl.close()
			elif command == '3':
				print(f'[{accent3} {tema}]При сбросе до заводских настроек тема и акценты сбрасываются до \n"по умолчанию", а также удаляются все приложения')
				print(f'[red {tema}]Вы хотите осуществить сброс до заводских настроек? (y/n)')
				command1 = input('>>>')
				if command1 == 'y':
					fl = open(f'{dirr}data//tema.nt', 'w')
					fl.write('')
					fl.close()
					fl = open(f'{dirr}data//accent.nt', 'w')
					fl.write('yellow')
					fl.close()
					fl = open(f'{dirr}data//accent2.nt', 'w')
					fl.write('blue')
					fl.close()
					fl = open(f'{dirr}data//accent3.nt', 'w')
					fl.write('green')
					fl.close()
					for i in apps:
						for j in listdir('apps//' + i):
							remove('apps//' + i + '//' + j)
						if i != 'Инструкция.txt':
							rmdir('apps//' + i)

					fl = open(f'{dirr}data//accent4.nt', 'w')
					fl.write('green')
					fl.close()
					fl = open(f'{dirr}code_.nt', 'a')
					fl.write('clear----')
					fl.close()
					print(f'[{accent2} {tema}]Настройки сброшены!')
				elif command1 == 'n':
					print(f'[red {tema}]Отказано в доступе на изменение настроек in line 230 #004')
				else:
					print(f'[red {tema}]Неверная команда in line 232 #001')
			elif command == '4':
				print(f'[{accent2} {tema}]Уведомления об изменении файла запуска: {"По умолчанию" if upd_msg else "Отключены"}')
				print(f'[bold {accent2} {tema}]Введите номер команды (1: Изменить настройки уведомлений об изменении файла запуска, 2: Выйти)')
				command1 = input('>>>')
				if command1 == '1':
					print(f'[{accent} {tema}]Введите состояние уведомлений об изменении файла запуска (1: По умолчанию, 2: Отключено, 3: Выйти)')
					command2 = input('>>>>')
					if command2 == '1':
						fl = open(f'{dirr}data\\upd_msg.nt', 'w')
						fl.write('False')
						fl.close()
						print(f'[{accent3} {tema}]Настройки успешно изменены.')
					elif command2 == '2':
						fl = open(f'{dirr}data\\upd_msg.nt', 'w')
						fl.write('True')
						fl.close()
						print(f'[{accent3} {tema}]Настройки успешно изменены.')
					elif command2 == '3':
						pass
					else:
						print(f'[red {tema}]Неверная команда in line 253 #001')
				elif command1 == '2':
					pass
				else:
					print(f'[red {tema}]Неверная команда in line 257 #001')
			elif command == '5':
				fl = open(f'{dirr}data\\dev.nt', 'r', encoding='utf-8')
				#dev.nt
				#[green]Информация о разработчике:
				#[green]Автор NTphone 2: Насиров Тимур
				#[green]Дата рождения автора: 2013г.
				#[green]Другие проекты: SCreater, TSdelivery, NT 993 (on youtube) и другие
				#[green]Первая версия NTphone (1.0) была выпущена примерно 10 марта 2023г. 
				print(fl.read())
				fl.close()
			elif command == '6':
				fl = open(f'{dirr}data\\info.nt', 'r', encoding='utf-8')
				#info.nt
				#[green]Информация о телефоне
				#[green]Версия NTphone: 2.0 beta
				#[green]Дата выхода этой версии: 10.10.23
				#[green]Дата выхода этой подверсии: 10.10.23
				#[green]Примерная дата выхода следующей подверсии: 17.10.23
				#[green]Сборка python: 3.11.0, 3.11.2
				#[green]Строк: 371
				#[green]Вес: 14.5КБ
				#[green]Код к удалению:17543
			elif command == '7':
				print(f'[red {tema}]Вы действительно хотите удалить NTphone 2? (y/n)')
				command1 = input('>>>')
				if command1 == 'y':
					print(f'[red {tema}]Недостаточно прав на удаление in line 284 #013')
				elif command1 == 'n':
					print(f'[red {tema}]Отказано в доступе на изменение настроек in line 286 #004')
				else:
					print(f'[red {tema}]Неверная команда in line 288 #001')
			else:
				print('Неверная команда in line 290 #001')
		def app(self):
			if apps == []:
				print(f'[red {tema}]В папке не найдено приложений in line 293 #003')
			else:
				print(f'[{accent} {tema}]Введите номер команды:')
				print(f'[bold {accent} {tema}]1: Посмотреть информацию о приложении')
				print(f'[bold {accent} {tema}]2: Посмотреть исходный код')
				print(f'[bold {accent} {tema}]3: Удалить приложение')
				upd()
				command = input('>>')
				print(f'[{accent2} {tema}] Выберите приложение: (введите имя папки)')
				print(apps)
				command1 = input('>>')
				if command1 in apps:				
					if command == '1':
						fl = open(f'{command1}\\info.nti', 'r', encoding='utf-8')
						print(f'[{accent3} {tema}]{fl.read()}')
						fl.close()
					elif command == '2':
						fl = open(f'{command1}\\main.py', 'r')
						print(f'[{accent3} {tema}]{fl.read()}')
						fl.close()
					elif command == '3':
						os.remove(f'\\apps/{command1}')
						print(f'[{accent} {tema}] Приложение удалено.')
		def open_app(self):
			upd()
			if apps == []:
				print(f'[red {tema}]В папке не найдено приложений in line 319 #003')
			else:
				print('Выберите приложение, которое хотите открыть')
				print(apps)
				command1 = input('>>')
				if command1 in apps:
					from open_app import start_app
					start_app(command1, dirr)
					upd()
				else:
					print(f'[red {tema}]Приложение не найдено in line 329 #003')
		def exit(self):
			raise ExitUserError('Пользователь вышел из телефона in line 331 #000')
			quit()

	#time
	def cur_time():
		from datetime import datetime
		now = datetime.now()
		print(now.strftime("%H:%M:%S"))

	#menu
	def menu():
		print(f'[{accent2} {tema}]ГЛАВНОЕ МЕНЮ')
		cur_time()
		print(f'[{accent3} {tema}]Введите номер команды:')
		print(f'[bold {accent} {tema}]1: Калькулятор')
		print(f'[bold {accent} {tema}]2: Секундомер')
		print(f'[bold {accent} {tema}]3: Проводник')
		print(f'[bold {accent} {tema}]4: Приложения')
		print(f'[bold {accent} {tema}]5: Настройки')
		print(f'[bold {accent} {tema}]6: Открыть приложение')
		print(f'[bold {accent} {tema}]7: Выключить телефон')

	#comand of input
	def start():
		command = input('>')
		c = Comand()
		if command == '1':
			c.calculator()
			upd()
		elif command == '2':
			c.secundomer()
			upd()
		elif command == '3':
			c.file_manager()
			upd()
		elif command == '4':
			c.app()
			upd()
		elif command == '5':
			c.settings(tema)
			upd()
		elif command == '6':
			c.open_app()
			upd()
		elif command == '7':
			c.exit()
			upd()
		else:
			print(f'[red {tema}]Неверная команда in line 379 #001')

	#start
	print('[blue]Добро пожаловать в NTphone 2!')
	while True:
		menu()
		start()
except ValueError:
	print('[red]Ошибка в значениях переменной in line 387 #009')
except FileNotFoundError:
	print('[red]Файлы не найдены (FileNotFound) in line 389 #006')
except ModuleNotFoundError:
	print('[red]Не установлены необходимые модули (ModuleNotFound) in line 391 #006')
except SyntaxError:
	print('[red]Ошибка в синтаксе (Ошибка в коде телефона) in line 393 #007')
except UnicodeDecodeError:
	print('[red]Ошибка при чтении файлов (UnicodeDecode) in line 395 #008')
except UnicodeEncodeError:
	print('[red]Ошибка при чтении файлов (UnicodeEncode) in line 397 #008')
except NameError:
	print('[red]Переменная\функция\класс\метод\аргумент не найден (Ошибка в коде телефона) in line 399 #007')
except KeyError:
	print('[red]Ошибка при вводе ключа для словаря (Ошибка в коде телефона) in line 401 #007')
except TabError:
	print('[red]Ошибка в табуляции (Ошибка в коде теллефона) (Tab) in line 403 #007')
except TypeError:
	print('[red]Ошибка в типе данных in line 405 #005')
except IndexError:
	print('[red]Индекс в последовательности вышел из допустимого диапазона in line 407 #010')
except KeyboardInterrupt:
	print('[red]Пользователь вышел из телефона стоп-комбинацией (Ctrl+C) in line 409 #000')
except EOFError:
	print('[red]Предел ввода информации in line 411 #011')
except MemoryError:
	print('[red]Закончилась память in line 413 #012')
except OSError:
	print('[red]Сбой системы in line 415 #012')
except OverflowError:
	print('[red]Слишком большой вывод арифметической операции in line 417 #010')
except IndentationError:
	print('[red]Ошибка в табуляции (Ошибка в коде теллефона) (Indenation) in line 419 #007')
except UnicodeError:
	print('[red]Ошибка при чтении файла (Unicode) in line 421 #008')
except UnicodeTranslateError:
	print('[red]Ошибка при чтении файла (Unicode) in line 423 #008')
except ImportError:
	print('[red]Не установлены необходимые модули (Import) in line 425 #006')



#print('Hello word')