# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat):
	dat.clear()
	n = int(op('inputInfo')['inputCount'] or 0)
	stepStmt = _prepStatement(parent().par.Stepstmt)
	initMode = parent().par.Initmode
	if initMode == 'firststep':
		if n == 0:
			return _prepStatement(parent().par.Defaultstmt)
		firstStmt = _prepStatement(parent().par.Firststepstmt)
		if n == 1:
			return _injectIndex(firstStmt, 1)
		lines = [_injectIndex(firstStmt, 1)] + [
			_injectIndex(stepStmt, i)
			for i in range(2, n + 1)
		]
	else:  # separate
		startStmt = _prepStatement(parent().par.Startstmt)
		lines = [startStmt] + [
			_injectIndex(stepStmt, i)
			for i in range(1, n + 1)
		]
	dat.write('\n'.join(lines))

def _injectIndex(code: str, i: int):
	return code.replace('$', str(i))

def _prepStatement(stmt: 'Par'):
	stmt = str(stmt)
	if not stmt:
		return ''
	if not stmt.endswith(';'):
		return stmt + ';'
	return stmt
