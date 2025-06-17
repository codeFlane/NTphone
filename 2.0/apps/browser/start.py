from webbrowser import open
from time import sleep
while True:
    print('Введите запрос:')
    search = input('>>browser>')
    print('Загрузка...')
    sleep(0.7)
    open(f'https://ya.ru/search/?text={search}')