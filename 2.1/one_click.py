print('Загрузка базы данных...')
from data.CreateDB import Create_DB
Create_DB()
from data.UseDB import Use_DB
db = Use_DB()
db.create_line(['accent', 'blue'])
db.create_line(['accent2', 'yellow'])
db.create_line(['accent3', 'green'])
db.create_line(['accent4', 'green'])
db.create_line(['tema', 'black'])
db.create_line(['upd-msg', False])
db.close_db()

print('Загрузка модулей...')
from os import system
system('pip install rich')
system('pip install pyautogui')

print('Проверка наличия модулей...')
from os import listdir
LD = listdir(__file__[0:__file__.find('one_click.py')])
if 'main.py' in LD and 'opent.py' in LD and 'apps' in LD and 'data' in LD and 'open_app.py' in LD and 'code_.nt' in LD:
	print('Успешно!')
else:
	print('Некоторые модули удалены! Переустановите NTphone')