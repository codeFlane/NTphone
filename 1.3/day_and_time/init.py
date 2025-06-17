from day_and_time import calindar
from rich import print
from time import time
print('[green]Day and time')
print('[bold black]program for NTphonePy')
print(f'Век: {calindar.leap}')
print(f'Год: {calindar.year}')
print(f'Месяц: [bold cyan]{calindar.month_(calindar.month)}')
print(f'День недели: [bold cyan]{calindar.week}')
print(f'День: {calindar.day}')
print(f'Час: {calindar.hour}')
print(f'Минута: {calindar.minute}')
print(f'Секунда: {calindar.second}')
print(f'Микросекунда: {calindar.microsec}')

month = str(calindar.month_(calindar.month))
day = int(calindar.day)
hour = int(calindar.hour)
minute = int(calindar.minute)
sec = int(calindar.second)
microsec = int(calindar.microsec)
ocmd = ''

while ocmd != './exit':
	print('[yellow]Нажите Enter, чтобы обновить данные, или ./exit, чтобы выйти.')
	a = time()
	ocmd = input('day and time>  ')
	if ocmd == './exit':
		break
	else:
		b = time()
		c = round(b - a, 3)
		d = round(c)/60
		sec = round(sec + d)
		microsec = c
		while microsec >= 1:
			microsec = microsec - 1
			sec = sec + 1
		while sec >= 60:
			minute = minute + 1
			sec = sec - 60
		while minute > 60:
			hour = hour + 1
			minute = minute - 60
		while hour >= 24:
			day = day + 1
			hour = hour - 24
		while month == 'Декабрь':
			while day >= 31:
				month = 'Январь'
				day = 1
		print(f'Месяц: [bold cyan]{month}')
		print(f'День: {day}')
		print(f'Час: {hour}')
		print(f'Минута: {minute}')
		print(f'Секунда: {sec}')