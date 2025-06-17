from playsound import *
from rich import print
def start():
	print('  ^^^^^^^^^^^^^')
	print('[red]      _____')
	print('[red]    _/     \_')
	print('[red]   /[yellow] _______ \ ')
	print('[red]  | [yellow]|_______| |     [cyan]BOOM!!')
	print('[red]   \__     __/')
	print('[dim yellow]      |   |')
	print('[yellow]      |   |')
	print('[yellow]      |   |')
	print('[yellow]      |   |')
	print('[dim green]     /     \ ')
def music():
	playsound('animations\\explos.mp3', False)