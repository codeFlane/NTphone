from rich.console import Console
import os
c = Console()
def start():
	c.print('[bold black]program for xtype-code NTphone')
	c.print('[cyan]file os/init.py')
	while True:
		c.print('[magenta]Введите команду (-deldir -delfile -os -idpr -crdir -dop ./exit):')
		oacmd = input('os>')
		if oacmd == 'deldir':
			c.print('[cyan]Введите назавние директории папки вместе с ней [red](обратите внимание, папка должна быть пуста!)')
			noacmd = input('os>>')
			try:
				os.rmdir(noacmd)
				ans = noacmd[noacmd.rfind('\ '[0]):len(noacmd)]
				c.log('Папка "' + ans + '" успешно удалена.')
			except:
				c.log('[red]Ошибка! Введена неверная директория.')

		elif oacmd == 'delfile':
			c.print('[cyan]Введите директорию файла и его назавание:')
			noacmd = input('os>>')
			try:
				os.remove(noacmd)
				ans = noacmd[noacmd.rfind('\ '[0]):len(noacmd)]
				c.log('Папка "' + ans + '" успешно удалена.')
			except:
				c.log('[red]Ошибка! Введена неверная директория.')
		elif oacmd == 'os':
			c.print('[green]Ваша операционная система:')
			if os.name == 'nt':
				c.print('[cyan]Windows --nt--')
			elif os.name == 'posix':
				c.print('[yellow]POSIX standart')
			elif os.name == 'os2':
				c.print('[bold black] old, old, old OS/2')
			elif os.name == 'ce':
				c.print('[magenta]Windows Compact Embedded')
			elif os.name == 'java':
				c.print('[bold red]java OS')
			elif os.name == 'mac':
				c.print('[blue]OS X  --mac os--')
			elif os.name == 'riscos':
				c.print('[red]RISC os')
			else:
				c.print('[red]Программа не смогла определить операционую систему.')
				c.print(os.name)
		elif oacmd == 'idpr':
			c.print('[green]текущий id процессора: ' + str(os.getpid()))
		elif oacmd == 'crdir':
			c.print('[green]Введите директорию папки, которую хотите создать. [cyan](Например: C:\\Users\\Admin\\op (создать папку op))')
			naacmd = input('os>>')
			try:
				os.mkdir(naacmd)
			except:
				c.log('[red]Ошибка! Введена неверная директория.')
		elif oacmd == 'dop':
			nm = {
					'Имя компьютера' : os.environ['COMPUTERNAME'],
					'Уровень процессора' : os.environ['PROCESSOR_LEVEL'],
					#'Имя сессии' : os.environ['SESSIONNAME'],
					'Системный диск' : os.environ['SYSTEMDRIVE'],
					'Имя пользователя' : os.environ['USERNAME'],
					##'Директория Python' : os.environ['WINGDB_PYTHON'],
					#'cookie' : os.environ['WINDOWS_SPAWNCOOKIE'],
					#'Количество переменных сред' : os.environ['WINDOWS_TRACING_FLAGS']
				}
			c.print(os.environ)#nm)
		elif oacmd == './exit':
			quit()
		else:
			c.log('[red]Введёной команды не существует.')