import os
import sys

while True:
    print('Введите номер команды:')
    print('1: Имя операционой системы') #sys platform
    print('2: Директория этого файла') #os getcwd() 
    print('3: Имена доступных модулей') #sys builtin_module_name
    print('4: Дескриптор DLL Python') #sys dllhandle
    print('5: Путь к интерпретатору Python') #sys executable
    print('6: Используемая кодировка') #sys getdefaultencoding()
    print('7: Лимит рекурсии') #sys getrecursionlimit()
    print('8: Запись байткодов Python (.pyc)') #sys dont_write_bytecode
    print('9: Версия Python') #sys version
    print('10: Переменные окуржения') #os environ
    print('11: ID поцессора') #os getpid() 
    print('12: Список файлов и папок в директории') #os listdir()
    print('13: Размер файла') #os path getsize()
    print('14: Выход')
    
    command_ = input('>>computer-info>')
    if command_ == '1':
        ans = sys.platform
        if ans == 'linux':
            print('Linux 2.x/3.x')
        elif ans == 'win32':
            print('Windows')
        elif ans == 'cygwin':
            print('Windows/Cygwin')
        elif ans == 'darwin':
            print('Mac OS X')
        elif ans == 'os2':
            print('OS2')
        elif ans == 'os2emx':
            print('OS2 EMX')
        else:
            print('[red]Ошибка при определении системы in line 37 [MODULE] #-001')
    elif command_ == '2':
        print(os.getcwd())
    elif command_ == '3':
        print(sys.builtin_module_names)
    elif command_ == '4':
        print(sys.dllhandle)
    elif command_ == '5':
        print(sys.executable)
    elif command_ == '6':
        print(sys.getdefaultencoding())
    elif command_ == '7':
        print(sys.getrecursionlimit())
    elif command_ == '8':
        if sys.dont_write_bytecode:
            print('Выключено')
        else:
            print('Включено')
    elif command_ == '9':
        print(sys.version)
    elif command_ == '10':
        print(os.environ)
    elif command_ == '11':
        print(os.getpid())
    elif command_ == '12':
        print('Введите директорию:')
        command_0 = input('>>computer-info>>')
        print(os.listdir(command_0))
    elif command_ == '13':
        print('Введите директорию и название файла:')
        command_0 = input('>>computer-info>>')
        print(os.path.getsize(command_0))
    elif command_ == '14':
        break
    else:
        print('[red]Неверная команда in line 72 [MODULE] #001')