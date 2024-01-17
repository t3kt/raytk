# noinspection PyUnreachableCode
if False:
	# noinspection PyUnresolvedReferences
	from _stubs import *

def onCook(dat):
	dat.clear()
	info = op('inputInfo')  # type: CHOP
	stepStmt = _prepStatement(parent().par.Stepstmt)
	initMode = parent().par.Initmode
	numMode = parent().par.Numberingmode
	startIndex = int(parent().par.Startindex)
	exprIndexOffset = int(parent().par.Exprindexoffset)
	if numMode == 'available':
		indices = [
			tdu.digits(ch.name)
			for ch in info.chans('hasInput*')[startIndex:]
			if ch
		]
		n = len(indices)
	else:  # sequential
		n = int((info['inputCount'] or 0 - startIndex))
		indices = list(range(startIndex + 1, startIndex + n + 1))
	if parent().par.Reverseorder:
		indices = list(reversed(indices))
	if initMode == 'firststep':
		if n == 0:
			dat.write(_prepStatement(parent().par.Defaultstmt))
			return
		firstStmt = _prepStatement(parent().par.Firststepstmt)
		if n == 1:
			dat.write(_injectIndex(firstStmt, indices[0] + exprIndexOffset))
			return
		lines = [_injectIndex(firstStmt, indices[0] + exprIndexOffset)] + [
			_injectIndex(stepStmt, i + exprIndexOffset)
			for i in indices[1:]
		]
	else:  # separate
		startStmt = _prepStatement(parent().par.Startstmt)
		lines = [startStmt] + [
			_injectIndex(stepStmt, i + exprIndexOffset)
			for i in indices
		]
	dat.write('\n'.join(lines))

def _injectIndex(code: str, i: int):
	return code.replace('$', str(i))

def _prepStatement(stmt: Par):
	stmt = str(stmt)
	if not stmt:
		return ''
	if not stmt.endswith(';') and '\n' not in stmt:
		return stmt + ';'
	return stmt
