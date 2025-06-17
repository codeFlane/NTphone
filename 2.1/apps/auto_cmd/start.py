dirr = __file__[0:__file__.find('start.py')]
fl = open(f'{dirr}data.nt', 'a')
try:
    from os import system
    from datetime import datetime
    def cur_time(): 
        now = datetime.now()
        return now.strftime("%H:%M:%S")
    while True:
        print('Введите команду для cmd: (введите /exit для выхода)')
        command_ = input('>>auto_cmd>')
        if command_ == '/exit':
            fl.close()
            break
        else:
            fl.write(cur_time() + ' ' +  command_ + '\n')
            system(command_)
except Exception:
    fl.close()
    print('error')
        