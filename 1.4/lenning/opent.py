def read(name):
	fl = open(f'lenning\\{name}.txt', 'r')
	ret = fl.read()
	fl.close()
	print(ret)
	return ret
def init_read(name):
	dr = __file__.find('none_init.py')
	dri = __file__[0:dr]
	c = '\ '[0]
	fl = open(f'{dri}{c}{name}.txt', 'r')
	ret = fl.read()
	fl.close()
	print(f'{dri}{c}{name}.txt')
	return ret