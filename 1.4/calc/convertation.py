typs = ['time', 'liquid', 'lenght', 'weight']
typs_liquid = ['ml', 'l']
typs_time = ['s', 'min', 'day', 'mn', 'yr', 'lp']
typs_weight = ['g', 'kg', 'c', 't']
typs_lenght = ['mm', 'cm', 'dm', 'm', 'km']

def typ(name):
	try:
		it = 0
		for i in typs_liquid:
			if typs_liquid[i] == name:
				it = 1
				cl = typs[0]
		for i in typs_weight:
			if typs_weight[i] == name:
				it = 1
				cl = typs[1]
		for i in typs_lenght:
			if typs_lenght[i] == name:
				it = 1
				cl = typs[2]
		for i in typs_time:
			if typs_time[i] == name:
				it = 1
				cl = typs[3]
		if it == 0:
			return 18
		else:
			return cl
	except:
		return 15
def errors(name):
	try:
		tp = typ(name)
		it = 0
		if tp == 'liquid':
			for i in typs_liquid:
				if tp == typs_liquid[i]:
					it = 1
				else:
					it = 0
		if tp == 'lenght':
			for i in typs_lenght:
				if tp == typs_lenght[i]:
					it = 1
				else:
					it = 0
		if tp == 'weight':
			for i in typs_weight:
				if tp == typs_weight[i]:
					it = 1
				else:
					it = 0
		if tp == 'time':
			for i in typs_time:
				if tp == typs_time[i]:
					it = 1
				else:
					it = 0
		if it == 1:
			pass
			return 1
		else:
			return 18
	except:
		return 15
def table_lenght():
	print('в\из mm          cm          dm          m           km')
	print('mm   1           -           -           -           -')
	print('cm   10          1           -           -           -')
	print('dm   100         10          1           -           -')
	print('m    1,000       100         10          1           -')
	print('km   1,000,000   100,000     10,000      1,000       1')
	print('к версии 1.5 таблица станет цветной...')
def table_liquid():
	print('в\из ml          l')
	print('ml   1           -')
	print('l    1,000       1')
	print('к версии 1.5 таблица станет цветной...')
def table_time():
	print('из\в sec         min         h           day         week        m           yr          lp')
	print('sec  1           60          3,600       86,400      604,800     2,629,746   31,536,000  3,155,695,200')
	print('min  -           1           60          1,440       10,080      43,829      525,600     52,594,920')
	print('h    -           -           1           24          168         730         8,760       876,582')
	print('day  -           -           -           1           7           30.5        365.3       365,524.25')
	print('week -           -           -           -           1           4.35        52.14       5,217.7')
	print('m    -           -           -           -           -           1           12          1,200')
	print('yr   -           -           -           -           -           -           1           100')
	print('lp   -           -           -           -           -           -           -           1')
	print('к версии 1.6 таблица станет цветной...')
def table_weight():
	try:
		from rich import print
		from rich.console import Console
		from rich.table import Table
		cons = Console()
		print('[red on white]BETA-TEST functional colored.')
		table = Table()
		table.add_column('из\в', style='cyan', justify='center')
		table.add_column('g', style='bold red', justify='center')
		table.add_column('kg', style='yellow', justify='center')
		table.add_column('c', style='green', justify='center')
		table.add_column('t', style='blue', justify='center')
		table.add_row('g', '1', '1,000', '100,000', '1,000,000')
		table.add_row('kg', '[red]-', '1', '100', '1,000')
		table.add_row('c', '[red]-', '[red]-', '1', '10')
		table.add_row('t', '[red]-', '[red]-', '[red]-', '1')
		cons.print(table)

		return 7
	except ImportError:
		return 22
	except:
		return 15
	'''print('    g           kg          c           t')
	print('g   1           1,000       100,000     1,000,000')
	print('kg  -           1           100         1,000')
	print('c   -           -           1           10')
	print('t   -           -           -           1')'''
def tables(name):
	if name == 'liq':
		table_liquid()
	elif name == 'len':
		table_lenght()
	elif name == 'wid':
		table_width()
	elif name == 'time':
		table_time()
	else:
		return 6
#weight
def from_g_to_kg(g):
	class_num = {'class':'g', 'type':'width', 'to':'kilogramm'}
	return g / 1_000
def from_g_to_c(g):
	class_num = {'class':'g', 'type':'width', 'to':'centner'}
	return g / 100_000
def from_g_to_t(g):
	class_num = {'class':'g', 'type':'width', 'to':'tonn'}
	return g / 1_000_000

def from_kg_to_c(kg):
	class_num = {'class':'kg', 'type':'width', 'to':'centner'}
	return kg / 100
def from_kg_to_t(kg):
	class_num = {'class':'kg', 'type':'width', 'to':'tonn'}
	return kg / 1_000

def from_c_to_t(kg):
	class_num = {'class':'c', 'type':'width', 'to':'tonn'}
	return kg / 10


#lenght
def from_mm_to_cm(mm):
	class_num = {'class':'mm', 'type':'lenght', 'to':'santimetr'}
	return mm / 10
def from_mm_to_dm(mm):
	class_num = {'class':'mm', 'type':'lenght', 'to':'decimetr'}
	return mm / 100
def from_mm_to_m(mm):
	class_num = {'class':'mm', 'type':'lenght', 'to':'metr'}
	return mm / 1_000
def from_mm_to_km(mm):
	class_num = {'class':'mm', 'type':'lenght', 'to':'kilometr'}
	return mm / 1_000_000
def from_cm_to_dm(cm):
	class_num = {'class':'cm', 'type':'lenght', 'to':'decimetr'}
	return cm / 10
def from_cm_to_m(cm):
	class_num = {'class':'cm', 'type':'lenght', 'to':'metr'}
	return cm / 100
def from_cm_to_km(cm):
	class_num = {'class':'cm', 'type':'lenght', 'to':'kilometr'}
	return cm / 100_000
def from_dm_to_m(dm):
	class_num = {'class':'dm', 'type':'lenght', 'to':'metr'}
	return dm / 10
def from_dm_to_km(dm):
	class_num = {'class':'dm', 'type':'lenght', 'to':'kilometr'}
	return dm / 10_000
def from_m_to_km(m):
	class_num = {'class':'m', 'type':'lenght', 'to':'kilometr'}
	return m / 10
def from_dm_to_m(dm):
	class_num = {'class':'dm', 'type':'lenght', 'to':'metr'}
	return dm / 10


#liquid
def from_ml_to_l(ml):
	class_num = {'class':'ml', 'type':'liquid', 'to':'litr'}
	return ml / 1_000

#time
def from_sec_to_min(sec):
	class_num = {'class':'sec', 'type':'time', 'to':'minute'}
	return sec / 60
def from_sec_to_h(sec):
	class_num = {'class':'sec', 'type':'time', 'to':'hour'}
	return sec / 3_600
def from_sec_to_day(sec):
	class_num = {'class':'sec', 'type':'time', 'to':'day'}
	return sec / 86_400
def from_sec_to_week(sec):
	class_num = {'class':'sec', 'type':'time', 'to':'week'}
	return sec / 604_800
def from_sec_to_m(sec):
	class_num = {'class':'sec', 'type':'time', 'to':'month'}
	return sec / 2_629_746
def from_sec_to_yr(sec):
	class_num = {'class':'sec', 'type':'time', 'to':'year'}
	return sec / 31_536_000
def from_sec_to_lp(sec):
	class_num = {'class':'sec', 'type':'time', 'to':'leap'}
	return sec / 3_155_695_200
def from_min_to_h(_min):
	class_num = {'class':'min', 'type':'time', 'to':'hour'}
	return _min / 60
def from_min_to_day(_min):
	class_num = {'class':'min', 'type':'time', 'to':'day'}
	return _min / 1_440
def from_min_to_week(_min):
	class_num = {'class':'min', 'type':'time', 'to':'week'}
	return _min / 10_080
def from_min_to_m(_min):
	class_num = {'class':'min', 'type':'time', 'to':'month'}
	return _min / 43_829
def from_min_to_yr(_min):
	class_num = {'class':'min', 'type':'time', 'to':'year'}
	return _min / 525_600
def from_min_to_lp(_min):
	class_num = {'class':'min', 'type':'time', 'to':'leap'}
	return _min / 1_440




def all_variables(a, tp):
	return 90
def the_error(cd):
	from rich import print
	if cd <= 10:
		print('[green]NoError.')
	if cd == 31:
		print('[red]MeraError. /')
	if cd == 15:
		print('[yellow]ExceptError. /')
	if cd == 18:
		print('[red]TypeConvError. /')
	if cd == 22:
		print('[red]InstallError. /')
	if cd == 44:
		print('[red]SysError. /')
	if cd == 90:
		print('[red]ProjectNotReadyError. /') 
#table_time()