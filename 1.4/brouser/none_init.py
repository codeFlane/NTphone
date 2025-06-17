from webbrowser import open as webs
def web(ii, coder):
	#print('python говно!!!!!!!!!!!! ', ii)
	if coder != './sets':
		if coder == './sets':
			return 1
		else:
			webs(ii)
			return 0
	else:
		return 1
from rich import print
from opent import init_py as init

b = init.rbruser()
gl = 'google'
ya = 'yandex'
ed = 'bing'
dk = 'duckgo'

print('[green]Brouser')
print('[bold black]program for NTphonePy')
while True:
	t = 0
	print('[yellow]Введите запрос, или "./sets" (settings) или "./exit" (exit)')
	cmd = input('brouser> ')
	if cmd == './sets':
		t = 1
		print('[green]Введите, что вы хотите настроить:')
		print('[cyan]-bruser (браузер по умолчанию)  [green]-searchs (запросы)')
		acmd = input('brouser>>  ')
		if acmd == 'bruser':
			print(f'[cyan]Выберите поисковик поумолчанию: (сейчас: {b})')
			print('[yellow]-google   [green]-bing   [red]-yandex   [bold yellow]-duckduckgo')
			xacmd = input('bruser>>>  ')
			if xacmd == 'google':
				init.wbruser('google')
				print('[yellow]brouser по умолчанию: Google Chrome')
				print('[green]Перезапустите приложение, чтобы действие заработало.')
				break
			if xacmd == 'bing':
				init.wbruser('bing')
				print('[green]brouser по умолчанию: Microsoft Bing')
				print('[green]Перезапустите приложение, чтобы действие заработало.')
				break
			if xacmd == 'yandex':
				init.wbruser('yandex')
				print('[bold yellow]brouser по умолчанию: Yandex')
				print('[green]Перезапустите приложение, чтобы действие заработало.')
				break
			if xacmd == 'duckduckgo':
				init.wbruser('duckgo')
				print('[bold yellow]brouser по умолчанию: DuckDuckGo')
				print('[green]Перезапустите приложение, чтобы действие заработало.')
				break
			else:
				print('[red]Введённого браузера не существует. /')
		if acmd == 'searchs':
			print('')
			print(f'[green]:|{init.rsearch()}')
			t = 1
		else:
			print('[red]Введённой команды не существует. /')
	if cmd == './exit':
		break
	if True:#cmd != './exit' or cmd != './sets' or t == 0:
		if True:#not cmd == './exit' or cmd == './sets' or t == 1:
			if b == gl:
				bcmd = f'https://www.google.com/search?q={cmd}&source=hp&ei=UsFWY7uaMIiQxc8Pq6OXyA8&iflsig=AJiK0e8AAAAAY1bPYvK9EPCKnEUNCVz6kh8eXicUxPfG&ved=0ahUKEwi7i4a7qPn6AhUISPEDHavRBfkQ4dUDCAg&uact=5&oq=333&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEIAEELEDMgsIABCABBCxAxCDATIICAAQgAQQsQMyCwgAEIAEELEDEIMBMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgsILhCABBCxAxDUAjoOCC4QgAQQsQMQgwEQ1AI6BQguEIAEOggIABCxAxCDAToLCC4QgAQQsQMQgwE6CAguEIAEELEDUABY7AJgmghoAHAAeACAAaMBiAGxApIBAzIuMZgBAKABAQ&sclient=gws-wiz'
				nn = web(bcmd, cmd)
				if nn == False:
					init.getsearch(cmd)
					print('[green]Направление на URL-адрес: ', bcmd, '')
				else:
					print('[red]Отказано на отправку на URL-адрес:', bcmd)
			if b == ya:
				bcmd = f'https://yandex.ru/search/?text={cmd}&lr=119687&clid=2411726'
				nn = web(bcmd, cmd)
				if nn == False:
					init.getsearch(cmd)
					print('[green]Направление на URL-адрес: ', bcmd, '')
				else:
					print('[red]Отказано на отправку на URL-адрес:', bcmd)
			if b == ed:
				bcmd = f'https://www.bing.com/search?q={cmd}&form=QBLH&sp=-1&pq=tstet&sc=10-5&qs=n&sk=&cvid=6FFC716C9DBD4DF4968A7C948A8DCA94&ghsh=0&ghacc=0&ghpl='
				nn = web(bcmd, cmd)
				if nn == False:
					init.getsearch(cmd)
					print('[green]Направление на URL-адрес: ', bcmd, '')
				else:
					print('[red]Отказано на отправку на URL-адрес:', bcmd)
			if b == dk:
				bcmd = f'https://duckduckgo.com/?q={cmd}&t=h_&ia=web&natb=v348-6__&cp=atbsc'
				nn = web(bcmd, cmd)
				if nn == False:
					init.getsearch(cmd)
					print('[green]Направление на URL-адрес: ', bcmd, '')
				else:
					print('[red]Отказано на отправку на URL-адрес:', bcmd)