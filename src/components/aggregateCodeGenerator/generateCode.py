# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat):
	dat.clear()
	n = int(op('inputInfo')['inputCount'] or 0)
	startStmt = str(parent().par.Startstmt)
	stepStmt = str(parent().par.Stepstmt)
	if not startStmt.endswith(';'):
		startStmt += ';'
	if not stepStmt.endswith(';'):
		stepStmt += ';'
	lines = [startStmt] + [
		stepStmt.replace("$", str(i))
		for i in range(1, n + 1)
	]
	dat.write('\n'.join(lines))
