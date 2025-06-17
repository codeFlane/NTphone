def nlen(ln):
	ln = len(str(ln))
	ln = int(ln)
	ln = ln - 19
	#ln = str(ln)
	ret = ln
	return ret
def troecrat(name):
	ln = len(name)
	if ln == 3 or ln == 6 or ln == 9 or ln == 12 or ln == 15 or ln == 18 or ln == 21 or ln == 24:
		return 1
	else:
		return 0
def for_troecrat(name):
	ln = len(name)
	if not troecrat(name):
		if ln == 4 or ln == 7 or ln == 10 or ln == 13 or ln == 16 or ln == 19 or ln == 22:
			return 1
		elif ln == 5 or ln == 8 or ln == 11 or ln == 14 or ln == 17 or ln == 20 or ln == 23:
			return 2
		else:
			return 0
	else:
		return 0