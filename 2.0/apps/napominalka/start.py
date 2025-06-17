from datetime import datetime
from pyautogui import alert
from os import listdir
from time import sleep
from rich import print
dirr = __file__[0:__file__.find('start.py')]
fl = open(f'{dirr}data.nt', 'r')
comand_000 = float(fl.read())
fl.close()
def cur_time(): 
	now = datetime.now()
	return now.strftime("%H:%M:%S")
def create_napom(name, text, date):
    print('[green]Напоминание создано!')
    print('[cyan]Не выключайте NTphone. (Если хотите выключить напоминание нажмите Ctrl+C и перезайдите)')
    while True:
        sleep(comand_000)
        if cur_time() == date:
            alert(text + '                                ', name)
            break
 
while True:
    print('[yellow]Выберите номер команды')
    print('[bold yellow]1: Создать напоминание')
    print('[bold yellow]2: Установить ожидание повторения')
    print('[bold yellow]3: Выход')
    command_ = input('>>napominalka>')
    if command_ == '1':
        print('[magenta]Введите название напоминания: (Напрмиер:магазин)')
        command_0 = input('>>napomialka>>')
        print('[blue]Введите текст напоминания (Например: Сходить за хлебом)')
        command_1 = 'Напоминание: ' + input('>>napominalka>>')
        print('[cyan]Введите дату срабатывания напоминания в формате ЧЧ:ММ:СС (Например: 10:30:00)')
        command_2 = input('>>napominalka>>')
        if command_2.find(':') != -1:
            create_napom(command_0, command_1, command_2)
        else:
            print('[red]Значение задано неверно in line 36 [MODULE] #-001')
    elif command_ == '2':
        print('[yellow]Введите время ожидания для повторения (При маленьком времени ожидания напоминание более точно срабатывает, но забирает много ресурсов, а при большом наоборот) (Не устанавливайте меньше 0 и небольше 1)')
        command_0 = float(input('>>napominalka>>'))
        if command_0 < 1.0 and command_0 > 0.0:
            fl = open('data.nt', 'w')
            fl.write(str(command_0))
            fl.close()
        else:
            print('[red]Значение задано неверно in line 45 [MODULE] #-001')
    elif command_ == '3':
        break
    else:
        print('[red]Неверная команда in line 49 [MODULE] #001')