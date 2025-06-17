import sqlite3
connect = sqlite3.connect('textes.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS notebook(
               id INTEGER PRIMARY KEY,
               heading TEXT,
               data TEXT
                )''')

while True:
    print('Введите номер команды:')
    print('1: Создать запись')
    print('2: Просмотреть запись')
    print('3: Просмотреть названия')
    print('4: Удалить запись')
    print('5: Выйти')
    command = input('>>notebook>')
    if command == '1':
        print('Введите название записи:')
        command_1 = input('>>notebook>>')
        print('Введите запись:')
        command_2 = input('>>notebook>>')
        cursor.execute(f'''INSERT INTO notebook(heading, data) VALUES('{command_1}', '{command_2}')''')
        cursor.execute('''SELECT * FROM notebook''')
        id_ = cursor.fetchall()[len(cursor.fetchall()) - 1][0]
        print(f'Запись создана. Номер записи: {id_}')
        connect.commit()
    elif command == '2':
        print('Введите номер записи:')
        command_1 = input('>>notebook>>')
        cursor.execute(f'''SELECT * FROM notebook WHERE id = {command_1}''')
        data = cursor.fetchall()
        id_ = int(command_1) - 1
        if len(data) < id_:
            head = data[id_][1]
            text = data[id_][2]
            print(' '*20 + head)
            print(text)
        else:
            print('Запись не найдена')
    elif command == '3':
        cursor.execute('''SELECT * FROM notebook''')
        data = cursor.fetchall()
        if data != []:
            for i in data:
                print(f'{i[0]}. {i[1]}')
        else:
            print('Записей не найдено')
    elif command == '4':
        print('Введите номер записи:')
        command_1 = input('>>notebook>>')
        cursor.execute(f'''DELETE FROM notebook WHERE id = {command_1}''')
        print('Запись удалена.')
        connect.commit()
    elif command == '5':
        connect.close()
        break