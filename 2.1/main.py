try: #opent
	db = None
	from rich import print
	from data.UseDB import Use_DB
	from os import listdir, rmdir, mkdir
	from time import time

	dirr = __file__[0:__file__.find('main.py')]
	apps = listdir(dirr + '\\apps\\')
	apps.remove('IMDT.py')
	apps.remove('__pycache__')
	db = Use_DB()

	accent = db.read_line('accent', 0)
	accent2 = db.read_line('accent2', 1)
	accent3 = db.read_line('accent3', 2)
	accent4 = db.read_line('accent4', 3)
	tema = 'on white' if db.read_line('tema', 4) == 'white' else ''
	
	class Comand:
		def calculator(self):
			print(f'[{accent} {tema}]Введите тип калькулятора:')
			print(f'[bold {accent} {tema}]1: Обычный калькулятор')
			print(f'[bold {accent} {tema}]2: Калькулятор деления с остатком')
			command = input('>>')
			if command == '1':
				print(f'[{accent2} {tema}]Введите пример:')
				command = input('>>>')
				try:
					print(eval(command))
				except ZeroDivisionError:
					print(f'[red {tema}]Деление на ноль in line 30 #002')
			elif command == '2':
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
		
						print(f'[{accent} {tema}]Ответ: {ans}')
						print(f'[{accent} {tema}]Остаток: {ans2}')
						print(f'[{accent3} {tema}]Старт-число: {num}')
				except TypeError:
					print(f'[red {tema}]Ошибка в значениях переменной in line 94 #005')
		def secundomer(self):
			from time import time
			print(f'[{accent} {tema}]Введите, до скольки округлить числа:')
			num = int(input('>>'))
			print(f'[{accent2} {tema}]Нажмите Enter для старта:')
			input('>>')
			a = time()
			print(f'[{accent2} {tema}]Нажмите Enter для остановки:')
			input('>>')
			b = time()
			print(f'[{accent3} {tema}]Время от начала до конца: {round(b-a, num)}')
		def file_manager(self):
			from os import mkdir, rmdir
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
				print('[red]Введена неверная команда in line 115 #001')
		def settings(self,tema):
			print(f'[{accent} {tema}]Введите номер команды:')
			print(f'[bold {accent} {tema}]1: Изменить тему')
			print(f'[bold {accent} {tema}]2: Изменить цветовые акценты')
			print(f'[bold {accent} {tema}]3: Сброс до заводских настроек')
			print(f'[bold {accent} {tema}]4: Информация о NTphone')
			print(f'[bold {accent} {tema}]5: Информация об ошибках')
			command = input('>>')
			if command == '1':
				print(f'[{accent2} {tema}]Выберите тему:')
				print(f'[bold {accent2} {tema}]1: Светлая')
				print(f'[bold {accent2} {tema}]2: Тёмная (стандарт)')
				print(f'[bold {accent2} {tema}]3: Выйти')
				command1 = input('>>>')
				if command1 == '1':
					print(f'[green {tema}]Установлена светлая тема.')
					print(f'[red {tema}]Внимание: Не устанавливайте белые акценты.')
					db.update_line('tema', 'white')
					print(f'[{accent3} {tema}]Настройки успешно изменены.')
				elif command1 == '2':
					print(f'[green {tema}]Установлена тёмная тема.')
					db.update_line('tema', 'black')
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
				command2 = input('>>>')
				
				n_comand = False
				if command2 == '1':
					color = 'red'
				elif command2 == '2':
					color = 'yellow'
				elif command2 == '3':
					color = 'green'
				elif command2 == '4':
					color = 'cyan'
				elif command2 == '5':
					color = 'blue'
				elif command2 == '6':
					color = 'magenta'
				elif command2 == '7':
					color = 'black'
				elif command2 == '8':
					color = 'white'
				elif command2 == '9':
					pass
					n_comand = True
				else:
					print(f'[red {tema}]Неверная команда in line 197 #001')
					n_comand = True

				if not n_comand:
					db.update_line(command1, color)
					print(f'[green {tema}]Настройки успешно изменены.')
			elif command == '3':
				print(f'[{accent3} {tema}]При сбросе до заводских настроек тема и акценты сбрасываются до \n"по умолчанию"')
				print(f'[red {tema}]Вы хотите осуществить сброс до заводских настроек? (y/n)')
				command1 = input('>>>')
				if command1 == 'y':
					db.update_line('accent', 'blue')
					db.update_line('accent2', 'cyan')
					db.update_line('accent3', 'green')
					db.update_line('accent4', 'green')
					db.update_line('tema', 'black')
					print(f'[green {tema}]Настройки сброшены!')
				elif command1 == 'n':
					print(f'[red {tema}]Отказано в доступе на изменение настроек in line 230 #004')
				else:
					print(f'[red {tema}]Неверная команда in line 232 #001')
			elif command == '4':
				from webbrowser import open
				open(f'{dirr}/html/index.html')
			elif command == '5':
				from webbrowser import open
				open(f'{dirr}/html/errors/index.html')
			else:
				print('Неверная команда in line 290 #001')
		def app(self):
			if apps == []:
				print(f'[red {tema}]В папке не найдено приложений in line 293 #003')
			else:
				from webbrowser import open
				print(apps)
				print(f'[{accent} {tema}]Введите номер команды:')
				print(f'[bold {accent} {tema}]1: Посмотреть информацию о приложении')
				print(f'[bold {accent} {tema}]2: Выйти')

				command = input('>>')
				print(f'[{accent2} {tema}] Выберите приложение: (введите имя папки)')
				command1 = input('>>')
				if command1 in apps:				
					if command == '1':
						fl = dirr + command1 + "\\info.nti"
						open(f'{dirr}html\\apps\\{command1}\\index.html')
					elif command == '2':
						pass
		def open_app(self):
			if apps == []:
				print(f'[red {tema}]В папке не найдено приложений in line 319 #003')
			else:
				print('Выберите приложение, которое хотите открыть')
				print(apps)
				command1 = input('>>')
				if command1 in apps:
					from open_app import start_app
					start_app(command1, dirr)
	
				else:
					print(f'[red {tema}]Приложение не найдено in line 329 #003')
		def exit(self):
			print('[red]Пользователь вышел из телефона in line 331 #000')
			quit()

	def menu():
		from datetime import datetime
		print(f'[{accent2} {tema}]ГЛАВНОЕ МЕНЮ')
		now = datetime.now()
		print(now.strftime("%H:%M:%S"))
		print(f'[{accent3} {tema}]Введите номер команды:')
		print(f'[bold {accent} {tema}]1: Калькулятор')
		print(f'[bold {accent} {tema}]2: Секундомер')
		print(f'[bold {accent} {tema}]3: Проводник')
		print(f'[bold {accent} {tema}]4: Приложения')
		print(f'[bold {accent} {tema}]5: Настройки')
		print(f'[bold {accent} {tema}]6: Открыть приложение')
		print(f'[bold {accent} {tema}]7: Выключить телефон')

	def start():
		command = input('>')
		c = Comand()
		if command == '1':
			c.calculator()
		elif command == '2':
			c.secundomer()
		elif command == '3':
			c.file_manager()
		elif command == '4':
			c.app()
		elif command == '5':
			c.settings(tema)
		elif command == '6':
			c.open_app()
		elif command == '7':
			c.exit()
		else:
			print(f'[red {tema}]Неверная команда in line 379 #001')

	print('[blue]Добро пожаловать в NTphone 2!')
	while True:
		menu()
		start()
except ValueError:
	print('[red]Ошибка в значениях переменной in line 387 #005')
except FileNotFoundError:
	print('[red]Файлы не найдены (FileNotFound) in line 389 #006')
except ModuleNotFoundError:
	print('[red]Модули не найдены (ModuleNotFound) in line 391 #006')
except SyntaxError:
	print('[red]Ошибка в синтаксе (Ошибка в коде телефона) in line 393 #007')
except UnicodeDecodeError:
	print('[red]Ошибка при чтении файлов (UnicodeDecode) in line 395 #008')
except UnicodeEncodeError:
	print('[red]Ошибка при чтении файлов (UnicodeEncode) in line 397 #008')
except NameError:
	print('[red]Переменная\функция\класс\метод\аргумент не найден (Ошибка в коде телефона) in line 399 #006')
except KeyError:
	print('[red]Ошибка в ключе для словаря (Ошибка в коде телефона) in line 401 #007')
except TabError:
	print('[red]Ошибка в табуляции (Ошибка в коде теллефона) (Tab) in line 403 #011')
except TypeError:
	print('[red]Ошибка в типе данных in line 405 #005')
except IndexError:
	print('[red]Индекс в последовательности вышел из допустимого диапазона in line 407 #010')
except KeyboardInterrupt:
	print('[red]Пользователь вышел из телефона стоп-комбинацией (Ctrl+C) in line 409 #000')
except EOFError:
	print('[red]Предел ввода информации in line 411 #010')
except MemoryError:
	print('[red]Закончилась память in line 413 #009')
except OSError:
	print('[red]Сбой системы in line 415 #012')
except OverflowError:
	print('[red]Слишком большой вывод арифметической операции in line 417 #010')
except IndentationError:
	print('[red]Ошибка в табуляции (Ошибка в коде теллефона) (Indenation) in line 419 #011')
except UnicodeError:
	print('[red]Ошибка при чтении файла (Unicode) in line 421 #008')
except UnicodeTranslateError:
	print('[red]Ошибка при чтении файла (Unicode) in line 423 #008')
except ImportError:
	print('[red]Не установлены необходимые модули (Import) in line 425 #006')
finally:
	db.close_db()


#print('Hello word')