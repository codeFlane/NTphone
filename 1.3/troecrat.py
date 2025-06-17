def nlen(ln):
	ln = int(ln)
	ln = ln - 15
	ln = str(ln)
	ret = len(ln)
	return ret + 1
def troecrat(name):
	ln = nlen(name)
	if ln == 3 or ln == 6 or ln == 9 or ln == 12 or ln == 15 or ln == 18:
		return 1
	else:
		return 0
def for_troecrat(name):
	ln = nlen(name)
	if not troecrat(name):
		if ln == 4 or ln == 7 or ln == 10 or ln == 13 or ln == 16:
			return 1
		elif ln == 5 or ln == 8 or ln == 11 or ln == 14 or ln == 17:
			return 2
		else:
			return 0
	else:
		return 0