from datetime import datetime
nw = datetime.now()


year = nw.year

year2 = year
if year2 > 2099:
	leap = 22
if year2 < 2099 and year2 > 2000:
	leap = 21
if year2 < 2000:
	leap = 20

month = nw.month
day = nw.day
hour = nw.hour
minute = nw.minute
second = nw.second
microsec = str(nw.microsecond)[0:3]

month2 = int(month)
day2 = int(day)
import calendar
a = calendar.weekday(year2,month2,day2)
days = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
week = days[a]

class SysMnError(Exception):
	...

def month_(name):
	name = str(name)
	if name == "1":
		return 'Январь'
	if name == "2":
		return "Февраль"
	if name == "3":
		return "Март"
	if name == '4':
		return "Апрель"
	if name == '5':
		return "Май"
	if name == '6':
		return "Июнь"
	if name == '7':
		return "Июль"
	if name == '8':
		return "Август"
	if name == '9':
		return "Сентябрь"
	if name == '10':
		return "Октябрь"
	if name == '11':
		return "Ноябрь"
	if name == '12':
		return "Декабрь"
	else:
		raise SysMnError('Системная ошибка.')