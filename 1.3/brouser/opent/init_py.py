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
def getsearch(data):
	fl = __file__.find('opend.py')
	fil = __file__[0:fl-9]
	c = '\ '[0]
	fl = open(f'{fil}{c}getsearch.txt', 'a')
	fl.write(f"'{data}'\n")
	fl.close()
def rsearch():
	fl = __file__.find('opend.py')
	fil = __file__[0:fl-9]
	c = "\ "[0]
	fl = open(f'{fil}{c}getsearch.txt', 'r')
	ret = fl.read()
	fl.close()
	return ret
def rbruser():
	fl = __file__.find('opend.py')
	fil = __file__[0:fl-9]
	c = "\ "[0]
	fl = open(f'{fil}{c}bruoser.txt', 'r')
	ret = fl.read()
	fl.close()
	return ret
def wbruser(br):
	fl = __file__.find('opend.py')
	fil = __file__[0:fl - 9]
	c = "\ "[0]
	fl = open(f'{fil}{c}bruoser.txt', 'w')
	fl.write(br)
	fl.close()